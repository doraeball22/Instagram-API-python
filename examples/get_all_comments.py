#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
from datetime import datetime
import json 

media_id = '2074063171660010833_18428658'

# stop conditions, the script will end when first of them will be true
until_date = '2019-07-31'
count = 100

API = InstagramAPI("slowlifecoding", "boncoding22")
API.login()
API.getUsernameInfo('kimkardashian')
has_more_comments = True
max_id = ''
comments = []

while has_more_comments:
    _ = API.getMediaComments(media_id, max_id=max_id)
    # comments' page come from older to newer, lets preserve desc order in full list
    for c in reversed(API.LastJson['comments']):
        comments.append(c)
        print(c)
    has_more_comments = API.LastJson.get('has_more_comments', True)
    # evaluate stop conditions
    # if count and len(comments) >= count:
    #     comments = comments[:count]
    #     print(json.dumps(comments[:count]))
    #     # stop loop
    #     has_more_comments = False
    #     print("stopped by count")
    # if until_date:
    #     older_comment = comments[-1]
    #     dt = datetime.utcfromtimestamp(older_comment.get('created_at_utc', 0))
    #     # only check all records if the last is older than stop condition
    #     if dt.isoformat() <= until_date:
    #         # keep comments after until_date
    #         comments = [
    #             c
    #             for c in comments
    #             # if datetime.utcfromtimestamp(c.get('created_at_utc', 0)) > until_date
    #         ]
    #         # stop loop
    #         has_more_comments = False
    #         print "stopped by until_date"
    #         print(c)
    # next page
    if has_more_comments:
        max_id = API.LastJson.get('next_max_id', '')
        time.sleep(2)

# print(json.dumps(comments))

with open('comments.json', 'w') as json_file:  
    json.dump(comments, json_file)