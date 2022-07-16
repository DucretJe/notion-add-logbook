# Create new entry in Notion LogBook

This scripts adds a new entry in a Database in Notion.
The usecase is to use it to create a new daily entry in a LogBook.

* Create a Notion integration
* Share a parent page of the DB with the integration

## How to

* Install dependencies

```sh
python3 -m pip install -r requirements.txt 
```

* Run it

```sh
python3 python/notion_add_entry -t <TOKEN> -n <DB_NAME>
```
