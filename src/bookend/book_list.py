#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
import json
import os.path


def list_file_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lists.json')


def init(path):
    if not os.path.isfile(path):
        book_list = create()
        save(path, book_list)
        print('Created new list file at ', path)


def create():
    return {
        'books': []
    }


def load(path):
    with open(path, 'r', encoding='UTF-8') as fh_list:
        return json.load(fh_list)


def save(path, book_list):
    with open(path, 'w', encoding='UTF-8') as fh_list:
        return json.dump(book_list, fh_list)


def list_books(book_list):
    return book_list['books']


def add_book(book_list, book):
    book_list['books'].append(book)
    return book_list


def remove_book(book_list, title):

    for i, book_item in enumerate(book_list['books']):
        if book_item['title'] == title:
            book_list['books'].pop(i)

    return book_list
