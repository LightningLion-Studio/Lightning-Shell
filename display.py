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
    print("输入`help`获得帮助\n")

def posts_dp():
    print("")
    get_posts("2")
    print("")

def posts_hot_dp():
    print("")
    get_posts("1")
    print("")

def read_post_dp():
    print("")
    id = input("-> 文章id=")
    print("")
    get_read_post(id)


def login():
    print("登陆时间：", time.asctime(time.localtime(time.time())))