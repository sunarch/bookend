#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from argparse import ArgumentParser
import logging

# imports: project
from bookend.structure import book
from bookend.structure import book_list


COMMAND_SEARCH = 'search'


def subparser_search(subparsers):
    parser: ArgumentParser = subparsers.add_parser(COMMAND_SEARCH)

    parser.add_argument(
        'query', metavar='Query',
        help='search for a term across all lists'
    )


def processor_search(data: dict, args):

    search_term = args.query.lower()
    results = []

    for book_item in book_list.list_books(data):

        found_in_fields = []

        for prop in book.properties_searchable():
            if search_term in book_item[prop].lower():
                found_in_fields.append(prop)

        if len(found_in_fields) > 0:
            results.append(book.formatted(book_item, found_in_fields))

    logging.info('Results for search term "%s"', args.query)

    for book_item in results:
        print(book_item)

    to_save = False
    return data, to_save
