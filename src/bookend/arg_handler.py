#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: project
from bookend import book
from bookend import book_list


def arg_add(book_list_path):
    data = book_list.load(book_list_path)
    book_item = book.input_book()
    book_list.add_book(data, book_item)
    book_list.save(book_list_path, data)


def arg_checkout(book_list_path, title):
    data = book_list.load(book_list_path)
    book_list.remove_book(data, title)
    book_list.save(book_list_path, data)


def arg_list(book_list_path):
    data = book_list.load(book_list_path)
    for book_item in book_list.list_books(data):
        print(book.formatted(book_item))


def arg_search(book_list_path, term):
    data = book_list.load(book_list_path)
    search_term = term.lower()
    results = []

    for book_item in book_list.list_books(data):

        found_in_fields = []

        for prop in book.properties_searchable():
            if search_term in book_item[prop].lower():
                found_in_fields.append(prop)

        if len(found_in_fields) > 0:
            results.append(book.formatted(book_item, found_in_fields))

    for book_item in results:
        print(book_item)
