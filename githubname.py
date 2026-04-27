import requests
import string
import time
import sys
import urllib3
import os
import threading
import itertools  # 引入迭代器工具，用于生成全排列

# ---------------- 配置区域 ----------------
PROXY_PORT = 7897
THREAD_COUNT = 10
# ----------------------------------------

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PROXIES = {
    "http": f"http://127.0.0.1:{PROXY_PORT}",
    "https": f"http://127.0.0.1:{PROXY_PORT}",
}

total_scanned = 0
found_count = 0
start_time = time.time()
found_names_set = set()
checked_names_set = set()  # 新增：记录已经检查过的名字（无论是否可用）
stop_event = threading.Event()

print_lock = threading.Lock()
file_lock = threading.Lock()


def load_history():
    """读取已发现的和已检查过的记录"""
    if os.path.exists("available_names.txt"):
        with open("available_names.txt", "r") as f:
            for line in f:
                name = line.strip()
                if name: found_names_set.add(name)

    # 建议手动创建一个 checked.txt 来保存所有试过的，防止重启脚本重头再来
    if os.path.exists("checked_history.txt"):
        with open("checked_history.txt", "r") as f:
            for line in f:
                name = line.strip()
                if name: checked_names_set.add(name)
    print(f"[*] 已加载历史：可用 {len(found_names_set)} 个，已尝试 {len(checked_names_set)} 个")


def save_available(username):
    with file_lock:
        if username not in found_names_set:
            found_names_set.add(username)
            with open("available_names.txt", "a") as f:
                f.write(f"{username}\n")


def save_checked(username):
    """记录已检查的任务，防止下次重启重复"""
    with file_lock:
        with open("checked_history.txt", "a") as f:
            f.write(f"{username}\n")


def check_github_username(username):
    url = f"https://github.com/{username}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        # 使用 verify=False 和代理
        response = requests.get(url, headers=headers, proxies=PROXIES, verify=False, timeout=8)
        if response.status_code == 404:
            return True
        elif response.status_code == 200:
            return False
        elif response.status_code == 429:
            return "LIMIT"
        return False
    except:
        return "ERROR"


def worker(name_list):
    """线程工作函数"""
    global total_scanned, found_count
    for username in name_list:
        if stop_event.is_set(): break

        # 跳过已检查的
        if username in checked_names_set:
            continue

        status = check_github_username(username)

        if status == "LIMIT":
            with print_lock:
                print(f"\n[!] 触发限流，等待 30 秒...")
            time.sleep(30)
            continue  # 稍后重试该名字，或者直接跳过

        total_scanned += 1
        save_checked(username)  # 无论成功失败都记录已检查

        if status is True:
            found_count += 1
            with print_lock:
                print(f"\n[★] 发现可用: {username}")
            save_available(username)

        # 频率控制：3位短ID检查过快易被封IP
        time.sleep(1.2)


def main():
    print("--- GitHub 3位纯字母用户名扫描器 ---")
    load_history()

    # 生成所有 3 位字母组合 (aaa, aab ... zzz)
    all_combinations = [''.join(p) for p in itertools.product(string.ascii_lowercase, repeat=3)]

    # 过滤掉已经检查过的
    remaining_tasks = [n for n in all_combinations if n not in checked_names_set]
    print(f"[*] 剩余待检查: {len(remaining_tasks)} / 17576")

    # 将任务分配给线程
    chunk_size = len(remaining_tasks) // THREAD_COUNT + 1
    threads = []
    for i in range(THREAD_COUNT):
        segment = remaining_tasks[i * chunk_size: (i + 1) * chunk_size]
        t = threading.Thread(target=worker, args=(segment,))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while any(t.is_alive() for t in threads):
            elapsed = time.time() - start_time
            speed = total_scanned / elapsed if elapsed > 0 else 0
            sys.stdout.write(
                f"\r[*] 进度: {total_scanned}/{len(remaining_tasks)} | 发现: {found_count} | 速度: {speed:.2f}/s")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        print("\n[*] 正在保存进度退出...")


if __name__ == "__main__":
    main()