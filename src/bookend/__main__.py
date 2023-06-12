#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from argparse import ArgumentParser

# imports: dependencies
from libmonty_logging.config.file_and_stream.v1 import config as logging_config
import libmonty_logging.helper as logging_helper
import libmonty_logging.message as logging_message

# imports: project
from bookend import version
from bookend import arg_handler


def main() -> None:

    logging_helper.apply_config(version.PROGRAM_NAME,
                                version.__version__,
                                logging_config)

    logging_message.program_header(version.PROGRAM_NAME)

    parser = ArgumentParser(prog=version.PROGRAM_NAME)

    parser.add_argument(
        '-v', '--version',
        help='Display version',
        action='store_true',
        dest='version'
    )

    option_group = parser.add_mutually_exclusive_group()

    option_group.add_argument(
        '-s', '--search', metavar='TERM',
        help='search for a term across all lists',
        dest='search', default=None
    )

    option_group.add_argument(
        '-l', '--list',
        help='prints a list of booklists',
        action='store_true',
        dest='list'
    )

    option_group.add_argument(
        '-a', '--add',
        help='add a new book!',
        action='store_true',
        dest='add'
    )

    option_group.add_argument(
        '-c', '--checkout', metavar='TITLE',
        help='enter the title of a book, and it\'ll be removed from the list',
        dest='checkout', default=None
    )

    args = parser.parse_args()

    if args.version:
        print(f'{version.PROGRAM_NAME} {version.__version__}')
        return

    if args.search is not None:
        arg_handler.arg_search(args.search)

    if args.list:
        arg_handler.arg_list()

    if args.add:
        arg_handler.arg_add()

    if args.checkout is not None:
        arg_handler.arg_checkout(args.checkout)


if __name__ == '__main__':
    main()

# -------------------------------------------------------------------- #
