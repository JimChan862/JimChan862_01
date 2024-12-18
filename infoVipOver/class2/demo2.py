import jsonpath

data={
    "store": {
        "book": [
            {
                "category": "新闻学",
                "author": "张三",
                "title": "图书标题1",
                "price": 8.95
            },
            {
                "category": "金融学",
                "author": "李四",
                "title": "图书标题2",
                "price": 12.00
            },
            {
                "category": "计算机",
                "author": "王五",
                "title": "图书标题3",
                "isbn": "0-553-21311-3",
                "price": 9.99
            },
            {
                "category": "医学",
                "author": "赵六",
                "title": "图书标题4",
                "price": 22.99
            }
        ],
        "phone": {
            "color": "red",
            "price": 1999.00,
            "author": "孙七"
        },
        "author": "周八",
        "price": 1.00
    },
    "author": "吴九"
}

# #  找出book的所有author  ['张三', '李四', '王五', '赵六']
# jsonpath(数据，表达式)
print(jsonpath.jsonpath(data,'$.store.book[*].author'))
# # # 所有节点下的author 只要是作者都找出..  ['吴九', '周八', '张三', '李四', '王五', '赵六', '孙七']
print(jsonpath.jsonpath(data,'$..author'))
# store下的所有元素
print(jsonpath.jsonpath(data,'$.store'))
# # book的第3个元素
print(jsonpath.jsonpath(data,'$.store.book[2]'))
# #  book的前面2个元素  切片  [开始值:结束值 不包含结束值]
print(jsonpath.jsonpath(data,'$.store.book[:2]'))
# # book的最后2个元素
print(jsonpath.jsonpath(data,'$.store.book[-2:]'))
# #  book的第1个元素到第4个元素  不包含4的元素
print(jsonpath.jsonpath(data,'$.store.book[:4]'))
# #  book中所有带有 isbn 的元素  [?(@.)]是过滤表达式的写法  [?(@.isbn)]过滤其他只找表示式里面的内容
print(jsonpath.jsonpath(data,'$.store.book[?(@.isbn)]'))

# 语法
# $ 整个根节点对象
# @ 当前节点
# .或[] 子节点
# * 任意子节点
# .. 任意后代节点