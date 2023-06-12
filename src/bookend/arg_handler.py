#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: project
from bookend.files import db
from bookend import book
from bookend import book_list


def arg_add():
    data = db.load()
    book_item = book.input_book()
    book_list.add_book(data, book_item)
    db.save(data)


def arg_checkout(title):
    data = db.load()
    book_list.remove_book(data, title)
    db.save(data)


def arg_list():
    data = db.load()
    for book_item in book_list.list_books(data):
        print(book.formatted(book_item))


def arg_search(term):
    data = db.load()
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
