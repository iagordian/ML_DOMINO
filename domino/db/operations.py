


from functools import wraps
from .base import get_db
from loger import connect_log, db_exception_log, \
    success_db_operation_log

from typing import Callable

def db_select(func: Callable) -> Callable:
    """
    Декоратор чтения данных из ДБ    
    Сгоздает объект сессии и передает в функцию в качестве аргумента
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            connect_log(func.__name__, args, kwargs)
            session = get_db()
            result = func(*args, db=session, **kwargs)

        except Exception as e:

            print('При работе с БД произошла ошибка', e)
            db_exception_log(func.__name__, e)         
            raise e
        
        else:
            success_db_operation_log()

        finally:
            session.close()

        return result

    return wrapper


def db_transaction(func: Callable) -> Callable:
    """
    Декоратор для взаимодействия с ДБ
    Попытка выполнить функцию-запрос к БД
    В случае успеха делает commit, в случае неудачи - rollback
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        session = get_db()

        try:
            connect_log(func.__name__, args, kwargs, select=False)
            res = func(*args, db=session, **kwargs)
            session.commit()
                    
        except Exception as e:

            session.rollback()
            db_exception_log(func.__name__, e, select=False)
            print('При работе с БД произошла ошибка', e)
            
            raise e
        
        else:
            success_db_operation_log()
        
        finally:
            session.close()

        return res
    
    return wrapper
