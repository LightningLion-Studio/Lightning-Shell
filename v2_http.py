import requests
import json

from html.parser import HTMLParser

class HTMLParser_v2(HTMLParser):
    def handle_data(self, data):
        print(":", data)

api = "https://v2.api.light.xhhzs.cn/v2/"

def get_announcement():
    try:
        get_data = requests.get(api+"announcement")
    except KeyError:
        print("错误:您可能没有连接网络或网络超时")
        exit()
    json_data = get_data.json()
    announcement = json_data["data"]
    return announcement

def get_posts(posts_id):
    get_data = requests.get(api+"post?order="+posts_id)
    json_data = json.loads(get_data.text)
    titles = json_data.get("data")
    for i in titles:
        title=i.get("title")
        id=i.get("id")
        print(f"标题:{title}, id:{id}")

def get_read_post(post_id):
    get_data = requests.get(api+"post/single?id="+post_id)
    json_data = json.loads(get_data.text)
    text_data = json_data.get("data")
    try:
        text_title = text_data.get("title")
    except AttributeError:
        print("错误:无法获取到文章数据,请检查输入是否存在\n")
        return 1
    text_body = text_data.get("data")
    parser = HTMLParser_v2()
    print(f"\n{text_title}\n")
    parser.feed(text_body)