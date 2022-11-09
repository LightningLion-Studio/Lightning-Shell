import requests
import json


api = "https://v2.api.light.xhhzs.cn/v2/"

def get_announcement():
    get_data = requests.get(api+"announcement")
    json_data = get_data.json()
    announcement = json_data["data"]
    return announcement

def get_posts(posts_id):
    get_data = requests.get(api+"post?order="+posts_id)
    json_data = json.loads(get_data.text)
    titles = json_data.get('data')
    print("\n")
    for i in titles:
            title=i.get('title')
            id=i.get('id')
            print(f"|标题:{title}|id:{id}|")
    print("\n")