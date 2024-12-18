# c开发  首页 用到注册登录的功能数据
# 调用 接口 c开发调用ab开发的功能写完了模块  静静等着 ab开发  测试
# 调试
from infoVipOver.class4.demo1 import test_demo1
from infoVipOver.class4.demo2 import test_demo2


def fun():
    # res1 值 1    res2 值  1   2
    # 1  2  直接写数据  代码 创建数据  真实的场景  res1 别的开发 提供数据
    res1=test_demo1()
    res2=test_demo2()
    if res1 == res2:
        return 1
    else:
        return 2