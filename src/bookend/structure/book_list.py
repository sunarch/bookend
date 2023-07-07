#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


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
