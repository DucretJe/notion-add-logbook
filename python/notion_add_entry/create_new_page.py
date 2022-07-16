# coding=utf-8

import requests

from datetime import date

def compute_title():
    """
    Create title from the date
    Truncated month (3rd first letters)
    """
    today = date.today()
    m = today.strftime("%B")
    d = today.strftime("%d")
    m = m[:3]
    title = m + " " + d
    return title

def new_entry(token, id):
    """
    Add new entry with date as title
    """
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": {
            # "type": "database_id",
            "database_id": "e07a5c87-55b0-4d73-b126-65efa40d0bfc",
        },
        "properties": {
		    "Name": {
			    "title": [
				    {
					"text": {
						"content": compute_title()
					}
				}]
            }
		},
    }  
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token,
    }
    r = requests.post(url, json=payload, headers=headers)
    return r.text

# print(compute_title())
print(new_entry("secret_O8dEegCu4NHtXGHTDpYOBDU73vArGbUMldUZ5guVIHW", "e07a5c87-55b0-4d73-b126-65efa40d0bfc"))

