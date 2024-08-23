

import configparser

from domino.files_navigation import join_absolute_path

config = configparser.ConfigParser()
config.read('domino/config/config.ini')

RANDOM_SEED = int(config.get('RANDOM', 'seed'))

SQLALCHEMY_DATABASE_URL = config.get("DATABASE", "url")

DATA_PACKAGES_DIR = join_absolute_path(config.get('DIRS', 'data_packages'))
UPLOAD_LOG_DIR = join_absolute_path(config.get('DIRS', 'upload_log'))

LOG_FILE = join_absolute_path(config.get('LOGS', 'log_file_path'))


