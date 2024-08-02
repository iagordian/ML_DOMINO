
from schemas import PicturesLst
from db.crud import save_picture

def upload_pictures(json_str):

    pictures_data = PicturesLst.parse_raw(json_str).pictures

    for picture_data in pictures_data:
        save_picture(picture_data)