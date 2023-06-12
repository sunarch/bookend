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
from bookend.commands import SUBPARSER_ADDERS, PROCESSORS, COMMANDS
from bookend.files import config, db


def main() -> None:

    # logging

    logging_helper.apply_config(version.PROGRAM_NAME,
                                version.__version__,
                                logging_config)

    logging_message.program_header(version.PROGRAM_NAME)

    # arguments

    parser = ArgumentParser(prog=version.PROGRAM_NAME)

    parser.add_argument(
        '-v', '--version',
        help='Display version',
        action='store_true',
        dest='version'
    )

    subparsers = parser.add_subparsers(title='Commands', dest='command')
    for subparser_adder in SUBPARSER_ADDERS:
        subparser_adder(subparsers)

    args = parser.parse_args()

    # processing

    if args.version:
        print(f'{version.PROGRAM_NAME} {version.__version__}')
        return

    _ = config.load()

    if args.command in COMMANDS:
        data = db.load()

        data, to_save = PROCESSORS[args.command](data, args)

        if to_save:
            db.save(data)


if __name__ == '__main__':
    main()
