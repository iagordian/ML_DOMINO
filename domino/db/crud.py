
from sqlalchemy.orm import Session
from typing import List, ByteString, Dict

from domino.schemas import Picture as Picture, ML_Object, ML_ObjectsList, \
    ForestModelThreshold, ForestModelThresholdList
from domino.models import Picture as Picture_obj, ML_Object as ML_SQL, \
    ForestModelThreshold as ForestModelThreshold_SQL
from domino.db import db_transaction, db_select

@db_transaction
def save_picture(picture: Picture, db: Session):
    '''Сохраняет в БД изображение домино'''
    picture = Picture_obj(**picture.model_dump(exclude_none=True))
    db.add(picture)

@db_transaction
def save_threshold(threshold: ForestModelThreshold, db: Session):
    '''Сохраняет в БД изображение домино'''
    threshold = ForestModelThreshold_SQL(**threshold.model_dump(exclude_none=True))
    db.add(threshold)

@db_select
def get_all_pictures(db: Session) -> List[Picture]:
    '''Возвращает все изображения домино, сохраненные в БД'''
    return [Picture.from_orm(picture_obj) for picture_obj in db.query(Picture_obj).filter(Picture_obj.up != -1 and Picture_obj.down != -1)]

@db_select
def get_empty_picture(db: Session) -> Picture:
    '''Возвращает изображение незаполненной домино'''
    return Picture.from_orm(db.query(Picture_obj).filter(Picture_obj.up == -1 and Picture_obj.up == -1).first())

@db_transaction
def model_to_db(ml: ML_Object, db: Session):
    '''Сохраняет объект ML в БД'''
    db.query(ML_SQL).filter_by(model_name=ml.model_name).delete()
    obj = ML_SQL(**ml.model_dump(exclude_none=True))
    db.add(obj)

@db_select
def get_ml_learned(model_name: str, db: Session) -> ML_Object:
    '''Загружает объект ML из БД'''
    return ML_Object.from_orm(db.query(ML_SQL).filter_by(model_name=model_name).first())

@db_select
def get_all_ML_logs(db: Session) -> List[dict]:
    '''Возвращает все записи об обучении объектов ML'''
    logs = [log[0] for log in db.query(ML_SQL.logs) if log[0] is not None]
    logs.append(
        {'forest_model_thresholdes': {t.min_size: t.threshold for t in db.query(ForestModelThreshold_SQL).order_by(ForestModelThreshold_SQL.min_size)}}
    )
    return logs

@db_transaction
def set_best_model(model_name: str, db: Session):
    '''Устанавливают метку о лучшей модели классификации на указанную модель'''
    model = db.query(ML_SQL).filter_by(model_name=model_name).first()
    model.is_the_best_classifier_model = 1
    model.logs['is_the_best_classifier_model'] = True

@db_select
def get_best_classifier_model(db: Session) -> ML_Object:
    '''Возвращает из БД модель, помеченную как лучшая модель классификации'''
    return ML_Object.from_orm(db.query(ML_SQL).filter_by(is_the_best_classifier_model=1).first())

@db_select
def get_img_bytes(up: int, down: int, db: Session) -> ByteString:
    '''Возвращает байтовую строку с изображением указанной домино'''
    img = db.query(Picture_obj.img).filter_by(
        up=up, down=down
    ).first()
    return img[0]

@db_select
def get_all_models_data(db: Session) -> ML_ObjectsList:
    '''Возвращает описание всех моделей ML (все данные, кроме самой модели)'''

    models=[
        ML_Object.from_orm(model) for model in db.query(ML_SQL)
    ]

    models = ML_ObjectsList(
        models=models
    )
    return models

@db_transaction
def save_thresholdes(thresholdes: Dict[int, float], db: Session):
    '''Сохранение словаря порогов принятия решения для дерева решений в БД'''
    
    for size, threshold in thresholdes.items():

        db.query(ForestModelThreshold_SQL).filter_by(min_size=size).delete()

        threshold_obj = ForestModelThreshold(
            min_size=size,
            threshold=threshold
        )
        db.add(ForestModelThreshold_SQL(
            **threshold_obj.model_dump()
        ))

@db_select
def get_all_thresholdes(db: Session) -> ForestModelThresholdList:
    '''Возвращает все объекты threshold в виде одного объекта'''

    thresholdes = ForestModelThresholdList(
        thresholdes = [{
            'min_size': threshold.min_size,
            'threshold': threshold.threshold
        } for threshold in db.query(ForestModelThreshold_SQL)]
    )
    return thresholdes

@db_select
def get_threshold(size: int, db: Session) -> float:
    '''Возвращает значение порога для переданной выборки'''
    return db.query(ForestModelThreshold_SQL.threshold).filter(
        ForestModelThreshold_SQL.min_size >= size
    ).order_by(
        ForestModelThreshold_SQL.min_size
    ).first()[0]