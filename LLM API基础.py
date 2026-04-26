from openai import OpenAI

client = OpenAI()


prompt = """
生成5个AI创业标题
每个不超过10个字
"""

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":prompt}]
)

print(resp.choices[0].message.content)