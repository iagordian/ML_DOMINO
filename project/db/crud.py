
from sqlalchemy.orm import Session
from typing import List

from schemas import Picture as Picture, ML_Object
from models import Picture as Picture_obj, ML_Object as ML_SQL
from db import db_transaction, db_select

@db_transaction
def save_picture(picture: Picture, db: Session):
    picture = Picture_obj(**picture.model_dump(exclude_none=True))
    db.add(picture)

@db_select
def get_all_pictures(db: Session) -> List[Picture]:
    return [Picture.from_orm(picture_obj) for picture_obj in db.query(Picture_obj).filter(Picture_obj.up != -1 and Picture_obj.down != -1)]

@db_select
def get_empty_picture(db: Session) -> Picture:
    return Picture.from_orm(db.query(Picture_obj).filter(Picture_obj.up == -1 and Picture_obj.up == -1).first())

@db_transaction
def model_to_db(ml: ML_Object, db: Session):

    db.query(ML_SQL).filter_by(model_name=ml.model_name).delete()
    obj = ML_SQL(**ml.model_dump(exclude_none=True))
    db.add(obj)

@db_select
def get_ml_learned(model_name: str, db: Session) -> ML_Object:
    return ML_Object.from_orm(db.query(ML_SQL).filter_by(model_name=model_name).first())

@db_select
def get_all_ML_logs(db: Session) -> List[dict]:

    logs_arr = []
    for ml_obj in db.query(ML_SQL):
        logs = ml_obj.logs
        if logs is not None:
            logs_arr.append(logs)

    return logs_arr

@db_transaction
def set_best_model(model_name: str, db: Session):
    model = db.query(ML_SQL).filter_by(model_name=model_name).first()
    model.is_the_best_classifier_model = 1
    model.logs['is_the_best_classifier_model'] = True

@db_select
def get_best_classifier_model(db: Session) -> ML_Object:
    return ML_Object.from_orm(db.query(ML_SQL).filter_by(is_the_best_classifier_model=1).first())