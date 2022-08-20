#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
import os

# imports: dependencies
from termcolor import colored


def input_book():
    title = input('Title: ')
    author = input('Author: ')
    call_number = input('Call Number: ')
    booklist = input('List Name: ')

    return create_book(
        title=title,
        author=author,
        call_number=call_number,
        booklist=booklist
    )


def create_book(title, author, call_number, booklist):
    return {
        'title': title,
        'author': author,
        'call_number': call_number,
        'booklist': booklist
    }


def searchable_properties():
    return {'title', 'author', 'booklist'}


def formatted(book, highlight=None):

    if not isinstance(highlight, list):
        highlight = []

    title = book['title']
    if 'title' in highlight:
        title = colored(book['title'], 'green')

    author = book['author']
    if 'author' in highlight:
        author = colored(book['author'], 'green')

    booklist = book['booklist']
    if 'booklist' in highlight:
        booklist = colored(book['booklist'], 'green')

    result = (
        ' ' * 4 + f'{"Title:":<13}{title}',
        ' ' * 4 + f'{"Author:":<13}{author}',
        ' ' * 4 + f'{"Call Number:":<13}{book["call_number"]}',
        ' ' * 4 + f'{"List:":<13}{booklist}'
    )

    return '\n' + os.linesep.join(result)
