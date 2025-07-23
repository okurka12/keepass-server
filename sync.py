import shutil
import config as conf

def get_latest():
    shutil.copy(conf.SYNC_PATH, conf.FILENAME)

def push_changes():
    shutil.copy(conf.FILENAME, conf.SYNC_PATH)
