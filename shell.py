from display import *
from v2_http import *

def shell(ish):
    _ish = ish
    if (_ish=="posts"):
        posts_dp()
    elif (_ish=="help"):
        print("""
posts: 获取文章（目前只能看到标题）
exit:  退出
        """)
    else:
        print("错误: 非法指令")