import time
from v2_http import *

Logo = """
 _     _       _     _         _             
| |   (_)     | |   | |       (_)            
| |    _  __ _| |__ | |_ _ __  _ _ __   __ _ 
| |   | |/ _` | '_ \| __| '_ \| | '_ \ / _` |
| |___| | (_| | | | | |_| | | | | | | | (_| | 
\_____/_|\__, |_| |_|\__|_| |_|_|_| |_|\__, |
          __/ |                         __/ |
         |___/                         |___/
"""

def home_dp():
    print(Logo)
    print("欢迎来到心电社区Shell版本 v1.0.1\n")
    print("公告:", get_announcement())
    print("输入指令以继续\n")

def posts_dp():
    print("输入1: 按热度排序 输入2: 按时间排序")
    posts_id = input("请输入你要获取的类型: ")
    print(get_posts(posts_id))

def login():
    print("登陆时间：", time.asctime(time.localtime(time.time())))