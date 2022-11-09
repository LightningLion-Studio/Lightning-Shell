from display import *
from v2_http import *

def shell(ish):
    _ish = ish
    if (_ish=="posts"):
        posts_dp()
    elif (_ish=="help"):
        print("""
posts: 获取文章列表
read_post: 阅读文章
exit:  退出
        """)
    elif (_ish=="read_post"):
        read_post_dp()
    else:
        print("错误: 非法指令")