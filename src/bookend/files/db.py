#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
import json
import logging
import os.path
import shutil

# imports: dependencies
from xdg_base_dirs import xdg_data_home

# imports: project
from bookend import version


def _data_dir_path() -> str:
    data_dir_path = os.path.join(xdg_data_home(), version.PROGRAM_NAME)

    if not os.path.isdir(data_dir_path):
        os.makedirs(data_dir_path, mode=0o740, exist_ok=True)

    return data_dir_path


def _data_file_name() -> str:
    return 'books.json'


def _data_file_path() -> str:
    data_file_path = os.path.join(_data_dir_path(), _data_file_name())

    if not os.path.isfile(data_file_path):
        with open(data_file_path, 'w', encoding='UTF-8') as fh_data:
            json.dump(empty_db(), fh_data, indent=2)
        logging.info('Created new data structure at "%s"', data_file_path)

    return data_file_path


def load() -> dict:
    data_file_path = _data_file_path()

    with open(data_file_path, 'r', encoding='UTF-8') as fh_data:
        logging.info('Loaded data from "%s"', data_file_path)
        return json.load(fh_data)


def save(config: dict) -> None:
    data_file_path = _data_file_path()
    backup_file_path = f'{_data_file_path()}.bak'

    shutil.copy2(data_file_path, backup_file_path)
    logging.info('Backed up data to "%s"', backup_file_path)

    with open(data_file_path, 'w', encoding='UTF-8') as fh_data:
        logging.info('Saved data to "%s"', data_file_path)
        json.dump(config, fh_data, indent=2)


def empty_db() -> dict:
    return {
        'books': []
    }
