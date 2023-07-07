#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
import os

# imports: dependencies
from termcolor import colored


fields = [
    {
        'name': 'title',
        'prompt': 'Title',
        'searchable': True
    },
    {
        'name': 'author',
        'prompt': 'Author',
        'searchable': True
    },
    {
        'name': 'call_number',
        'prompt': 'Call Number',
        'searchable': False
    },
    {
        'name': 'booklist',
        'prompt': 'List Name',
        'searchable': True
    }
]


def properties():
    return list(map(lambda x: x['name'], fields))


def properties_searchable():
    searchable_props = set(map(lambda x: x['name'] if x['searchable'] else None, fields))
    searchable_props.remove(None)
    return searchable_props


def input_book():
    prop_items = {}

    for field in fields:
        prop_items[field['name']] = input(field['prompt'] + ': ')

    return create_book(**prop_items)


def create_book(**kwargs):
    if not set(kwargs.keys()) == set(properties()):
        raise KeyError('Unrecognized key in book creation')

    return kwargs


def formatted(book, highlight=None):

    if not isinstance(highlight, list):
        highlight = []

    def format_item(field):
        prop = book[field['name']]
        if field['searchable'] and field['name'] in highlight:
            prop = colored(book[field['name']], 'green')
        return ' ' * 4 + f'{field["prompt"]:<13}{prop}'

    result = list(map(format_item, fields))

    return '\n' + os.linesep.join(result)
