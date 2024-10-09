
from domino.schemas import PicturesLst, ML_ObjectsList, RandomForestObjectsList
from domino.db import save_picture, model_to_db, random_forest_to_db

def upload_pictures(json_str):

    pictures_data = PicturesLst.parse_raw(json_str).pictures

    for picture_data in pictures_data:
        save_picture(picture_data)

def upload_models(json_str):

    ml_models_data = ML_ObjectsList.parse_raw(json_str).models

    for model_data in ml_models_data:
        model_to_db(model_data)

def upload_random_forest(json_str):

    ml_models_data = RandomForestObjectsList.parse_raw(json_str).models

    for random_forest_data in ml_models_data:
        random_forest_to_db(random_forest_data)


