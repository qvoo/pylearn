from lxml import etree
import requests


html_str="""

<!-- 练习 XPath 专用 HTML -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>XPath 练习页面</title>
</head>
<body>
    <h1 id="main-title"> XPath 练习测试页面 </h1>
    <p class="desc">这是一个用于练习 XPath 语法的 HTML 页面</p>

    <div class="container">
        <h2>编程语言列表</h2>
        <ul id="lang-list">
            <li class="item" data-id="1">Python</li>
            <li class="item" data-id="2">Java</li>
            <li class="item highlight" data-id="3">JavaScript</li>
            <li class="item" data-id="4">Go</li>
        </ul>
    </div>

    <div class="content">
        <h2>工具推荐</h2>
        <div class="tool" name="editor">VS Code</div>
        <div class="tool" name="ide">IDEA</div>
        <div class="tool" name="browser">Chrome</div>
        
        <a href="https://www.baidu.com">百度</a>
        <a href="https://www.google.com">谷歌</a>
    </div>

    <div id="footer">
        <p>© 2025 XPath 练习</p>
    </div>
</body>
</html>

"""

tree=etree.HTML(html_str) # 把要解析的数据传进去
print(tree)
# print(etree.tostring(tree)) #element 转成字符串

#tree =html html--->div--->----
print(tree.xpath('//h1')) #tree ==html


#etree 返回的是列表

print(tree.xpath('//h1'))

"""
/ 从当前节点选取直接节点直接节点 //从当前节点悬念去子孙节点
.   选取当前节点  ..选取当前节点的父节点    @ 选取属性

last() 选取最后一个
\* 匹配任何属性节点
| 选取若干节(多个规则去匹配元素)
"""

tree.xpath('//[@id="lang-list"]/@class')
tree.xpath('//[@id="lang-list"]/@href')
tree.xpath('//[@id="lang-list"][1]/@class')#[1] 索引取值 1表示获取第一个元素 xpath索引从1开始 ()提高优先值