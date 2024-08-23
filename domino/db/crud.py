
from sqlalchemy.orm import Session
from typing import List, ByteString

from domino.schemas import Picture as Picture, ML_Object, ML_Objects_List
from domino.models import Picture as Picture_obj, ML_Object as ML_SQL
from domino.db import db_transaction, db_select

@db_transaction
def save_picture(picture: Picture, db: Session):
    '''Сохраняет в БД изображение домино'''
    picture = Picture_obj(**picture.model_dump(exclude_none=True))
    db.add(picture)

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
    return [log[0] for log in db.query(ML_SQL.logs).filter(ML_SQL.logs is not None)]

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
def get_all_models_data(db: Session) -> ML_Objects_List:
    '''Возвращает описание всех моделей ML (все данные, кроме самой модели)'''

    models=[
        ML_Object.from_orm(model) for model in db.query(ML_SQL)
    ]
    for model in models:
        model.model_obj = model.model_obj is not None

    models = ML_Objects_List(
        models=models
    )
    return models