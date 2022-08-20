#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# previous license:
# Copyright (c) 2016 Anthony Pizzimenti - The MIT License (MIT)

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from termcolor import colored


def input_book():
    title = input('Title: ')
    author = input('Author: ')
    callnumber = input('Call Number: ')
    booklist = input('List Name: ')

    return create_book(
        title=title,
        author=author,
        callnumber=callnumber,
        booklist=booklist
    )


def create_book(title, author, callnumber, booklist):
    return {
        'title': title,
        'author': author,
        'callnumber': callnumber,
        'booklist': booklist
    }


def formatted(book, highlight=None):

    if not isinstance(highlight, list):
        highlight = []

    title = colored(book['title'], 'green') if 'title' in highlight else book['title']
    author = colored(book['author'], 'green') if 'author' in highlight else book['author']
    booklist = colored(book['booklist'], 'green') if 'booklist' in highlight else book['booklist']

    result = f'''
    Title:\t\t{title}
    Author:\t\t{author}
    Call Number:\t{book["callnumber"]}
    List:\t\t{booklist}
    '''

    return result
