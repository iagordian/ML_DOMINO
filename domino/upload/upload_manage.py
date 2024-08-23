
from domino.schemas import PicturesLst, ML_Objects_List
from domino.db import save_picture, model_to_db
from domino.config import DATA_PACKAGES_DIR
from domino.files_navigation import join_file_path

def upload_pictures(json_str):

    pictures_data = PicturesLst.parse_raw(json_str).pictures

    for picture_data in pictures_data:
        save_picture(picture_data)

def upload_models(json_str):

    ml_models_data = ML_Objects_List.parse_raw(json_str).models

    for model_data in ml_models_data:

        if model_data.model_obj:
            file_name = join_file_path(DATA_PACKAGES_DIR, f'{model_data.model_name}_bytes')
            with open(file_name, 'rb') as file:
                model_bytes = file.read()

            model_data.model_obj = model_bytes
        else:
            model_data.model_obj = None

        model_to_db(model_data)