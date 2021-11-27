#!/usr/bin/python
# -*- coding: UTF-8 -*-

picture = {
    "width": 200,
    "height": 300,
    "color": "red"
}

book = {
    "name": "语文",
    "score": 99,
    "teacher": "张老师",
    "cover": picture
}

print(book)

print(book.get("name"))

print(book.get("score"))

print(book.get("cover").get("color"))