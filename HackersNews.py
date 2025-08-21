import time
import requests


# apiのURL
TOPSTORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/"


def get_top_story_id_list(max_item=500):
    """トップページ記事の情報取得
    Args:
        max_item(int): 取得する記事の数（最大500）
    Returns:
        list:トップページに表示されるidのリスト
    """

    res = requests.get(TOPSTORIES_URL).json()
    return res[0:max_item]


def get_story_dict(id):
    """特定idの記事情報の取得
    Args:
        id(int):取得する記事のid
    Returns:
        dict:記事情報のdict
    """

    url = f"{ITEM_URL}{id}.json"
    return requests.get(url).json()


def formated_dict(dict):
    """特定idの記事情報の取得
    Args:
        id(dict):記事情報のdict
    Returns:
        dict:titleとlinkの辞書型
    """

    return {"title": dict["title"], "link": dict.get("url") or "None"}


def main():
    # 記事情報
    top_thirty_list = get_top_story_id_list(max_item=30)

    time.sleep(1)  # ここで1秒止まる

    # 記事の情報取得
    for id in top_thirty_list:
        item = get_story_dict(id)
        result = formated_dict(item)
        print(result)
        time.sleep(1)  # ここで1秒止まる


if __name__ == "__main__":
    main()
