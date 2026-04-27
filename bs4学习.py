from bs4 import BeautifulSoup
html="""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>BS4 爬虫练习页面</title>
</head>
<body>
    <h1 id="main-title">热门书籍推荐</h1>
    <p class="desc">这是一个用于 <span>BeautifulSoup4</span> 练习的测试页面</p>

    <!-- 分类列表 -->
    <div class="category">
        <h2>书籍分类</h2>
        <ul>
            <li>Python编程</li>
            <li>前端开发</li>
            <li>数据分析</li>
        </ul>
    </div>

    <!-- 书籍卡片 -->
    <div class="book-list">
        <div class="book-item" id="book1">
            <h3>Python编程：从入门到实践</h3>
            <p class="author">作者：埃里克·马瑟斯</p>
            <p class="price">价格：59.80 元</p>
            <a href="https://example.com/book1" class="detail-link">查看详情</a>
        </div>

        <div class="book-item" id="book2">
            <h3>JavaScript高级程序设计</h3>
            <p class="author">作者：尼古拉斯·泽卡斯</p>
            <p class="price">价格：129.00 元</p>
            <a href="https://example.com/book2" class="detail-linking">查看详情</a>
        </div>

        <div class="book-item" id="book3">
            <h3>利用Python进行数据分析</h3>
            <p class="author">作者：韦斯·麦金尼</p>
            <p class="price">价格：89.00 元</p>
            <a href="https://example.com/book3" class="detail-link">查看详情</a>
        </div>
    </div>

    <!-- 表格数据 -->
    <table border="1" id="book-table">
        <tr>
            <th>书名</th>
            <th>分类</th>
            <th>评分</th>
        </tr>
        <tr>
            <td>Python编程</td>
            <td>Python</td>
            <td>9.5</td>
        </tr>
        <tr>
            <td>JS高级设计</td>
            <td>前端</td>
            <td>9.2</td>
        </tr>
    </table>

    <!-- 隐藏文本 -->
    <div style="display: none">这是隐藏内容，爬虫也能提取！</div>
</body>
</html>"""




soup=BeautifulSoup(html,'html.parser') #html.parser 自带的解析器
print(soup.a) #拿到a标签  soup.标签名 只会获取文件的第一个标签
print(soup.a.attrs) #拿到a标签的属性
print(soup.a['href']) #拿到a标签的href属性值 https://example.com/book1
print(soup.a.attrs['href']) #拿到a标签的href属性值  https://example.com/book1

print(soup.a.string) #拿到a标签的文本内容  查看详情  只有在此标签下没有子标签或者子标签下没有文本内容时，才可以使用string方法获取文本内容
print(soup.a.text) #拿到a标签的文本内容  查看详情

print(soup.a.get_text) #拿到a标签的所以文本内容，包括子孙节点的内容

#soup.find_all('a',过滤条件)  #找到所有a标签

print(soup.find_all('a',class_="detail-linking")) #找到所有class=detail-linking的a标签


#soup.select() css选择器 匹配所有符合条件的
#id选择器
print(soup.select('a#link')) #找到id=link的a标签


# id选择器 用#    class选择器用.    后代 用空格隔开    子代 >
print(soup.select('p a '))
print(soup.select("p>a"))

