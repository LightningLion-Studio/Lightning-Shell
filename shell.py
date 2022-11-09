from display import *
from v2_http import *

def shell(ish):
    _ish = ish
    if (_ish=="help"):
        print("""
ls: 获取文章列表(按时间)
lsh: 获取文章列表(按热度)
rp: 阅读文章
exit:  退出
        """)
    elif (_ish=="ls"):
        posts_dp()
    elif (_ish=="lsh"):
        posts_hot_dp()
    elif (_ish=="rp"):
        read_post_dp()
    else:
        print("错误: 非法指令")