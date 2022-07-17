#!/usr/bin/env python3
# coding=utf-8

import argparse

from create_new_page import new_entry
from get_resource_id import get_id

parser = argparse.ArgumentParser(description="Add an entry in a given database")
parser.add_argument("-t", "--token", help="token", required=True)
parser.add_argument(
    "-n", "--name", help="name of the database to update", required=True
)
args = parser.parse_args()

# pylint: disable=invalid-name
if __name__ == "__main__":  # pragma: no cover
    token = args.token
    name = args.name
    print("Retrieving DB ID...")
    db_id = get_id(token, name)
    print("Done")
    print("Creating Entry")
    new_entry(token, db_id)
