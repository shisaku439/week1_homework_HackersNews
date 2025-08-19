import time
import requests


# apiのURLと取得記事数
TOPSTORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = " https://hacker-news.firebaseio.com/v0/item/"
MAX_ITEM = 30


# トップページ記事の情報取得
def get_top_story_id_list():
    return requests.get(TOPSTORIES_URL).json()


# 特定idの記事情報の取得
def get_story_dict(id):
    url = f"{ITEM_URL}{id}.json"
    return requests.get(url).json()


def main():
    # 記事情報
    topstories_list = get_top_story_id_list()
    top_thirty_list = topstories_list[0:MAX_ITEM]

    time.sleep(1)  # ここで1秒止まる

    # 記事の情報取得
    for id in top_thirty_list:
        item = get_story_dict(id)
        result = {"title": item["title"], "link": item.get("url") or "None"}
        print(result)
        time.sleep(1)  # ここで1秒止まる


main()
