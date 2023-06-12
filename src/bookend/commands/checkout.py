#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from argparse import ArgumentParser

# imports: project
from bookend import book_list


COMMAND_CHECKOUT = 'checkout'


def subparser_checkout(subparsers):

    parser: ArgumentParser = subparsers.add_parser(COMMAND_CHECKOUT)

    parser.add_argument(
        '-t', '--title', metavar='TITLE',
        help='enter the title of a book, and it\'ll be removed from the list',
        dest='title',
        required=True
    )


def processor_checkout(data: dict, args):

    book_list.remove_book(data, args.title)

    to_save = True
    return data, to_save
