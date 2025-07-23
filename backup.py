#
# This module backups the file before overwriting
#

import config as conf
import shutil
import time
import pathlib
import os

os.makedirs(conf.BACKUP_DIRECTORY, exist_ok=True)

def make_backup() -> None:
    """
    Backs up FILENAME to BACKUP_DIRECTORY (see config.py)
    """

    timestamp = int(round(time.time()))
    path_object = pathlib.Path(conf.FILENAME)
    base_filename = path_object.stem
    extension = path_object.suffix

    destination = \
        f"{conf.BACKUP_DIRECTORY}/{base_filename}-{timestamp}{extension}"

    shutil.copy(conf.FILENAME, destination)
