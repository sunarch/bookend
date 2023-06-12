#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from argparse import ArgumentParser
import logging

# imports: project
from bookend import book
from bookend import book_list


COMMAND_LIST = 'list'


def subparser_list(subparsers):
    _: ArgumentParser = subparsers.add_parser(COMMAND_LIST)


def processor_list(data: dict, _):

    logging.info('List of all books:')

    for book_item in book_list.list_books(data):
        print(book.formatted(book_item))

    to_save = False
    return data, to_save
