# coding=utf-8

import requests


def get_id(token, name):
    """
    Get ID of a Notion resource authenticating with given token (arg1)
    It uses a query (arg2)
    It uses filter (arg3)
    """
    url = "https://api.notion.com/v1/search"
    payload = {
        "page_size": 4,
        "query": name,
        "filter": {"value": "database", "property": "object"},
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token,
    }
    r = requests.post(url, json=payload, headers=headers)
    if len(r.json()["results"]) > 1:
        return "Different DB with same name detected"
    return r.json()["results"][0]["id"]
