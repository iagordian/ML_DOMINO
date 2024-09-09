
from domino.schemas import PicturesLst, ML_ObjectsList, ForestModelThresholdList
from domino.db import save_picture, model_to_db, save_threshold
from domino.config import DATA_PACKAGES_DIR
from domino.files_navigation import join_file_path

def upload_pictures(json_str):

    pictures_data = PicturesLst.parse_raw(json_str).pictures

    for picture_data in pictures_data:
        save_picture(picture_data)

def upload_models(json_str):

    ml_models_data = ML_ObjectsList.parse_raw(json_str).models

    for model_data in ml_models_data:
        model_to_db(model_data)

def upload_thresholdes(json_str):

    thresholdes_data = ForestModelThresholdList.parse_raw(json_str).thresholdes

    for threshold_data in thresholdes_data:
        save_threshold(threshold_data)

