
from config import LOG_FILE

import logging
import logging.handlers


log_format = "%(asctime)s ::%(levelname)s::"\
             " %(message)s"
fmtdate = '%d.%m.%Y %H:%M:%S'
formatter = logging.Formatter(log_format, fmtdate)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

file_handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=100000, backupCount=100)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def url_query_log(url: str, args: tuple):
    '''Записывает лог о запросе к API'''
    log = f'Запрос на URL "{url}"'
    if args:
        log += f' с передаваемыми данными {args}'
    log += '.\n'
    logger.info(log)

def server_error_log(url: str, exc: Exception):
    '''Записывает лог о произошедшей ошибке'''
    log = f'При обработке запроса на URL "{url}" произошла критическая ошибка. \nИнформация об ошибке: {repr(exc)}\n'
    logger.error(log)

def connect_log(func_name: str, args: tuple, kwargs: dict, select: bool=True):
    '''Записывает лог о соединении с БД'''    
    purpose = 'с целью извлечения данных' if select else 'с целью занесения данных'
    log = f'Функция {func_name} производит запрос к БД {purpose}'
    if args or kwargs:
        log += f'.\nВ функцию переданы аргументы {args} {kwargs}'
    logger.info(log + '.\n')

def db_exception_log(func_name: str, exc: Exception, select: bool=True):
    '''Записывает лог о неудочном запросе к БД'''
    purpose = 'с целью извлечения данных' if select else 'с целью занесения данных'
    log = f'При запросе функции к БД {func_name} {purpose} произошла ошибка {exc.__class__.__name__}.\nИнформация об ошибке: {repr(exc)}.\n'
    logger.error(log)

def success_db_operation_log():
    '''Записывает лог об успешном запросе к БД'''
    logger.info('Запрос к БД произведен успешно\n')