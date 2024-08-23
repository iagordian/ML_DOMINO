from .uploader import Uploader
from .upload_manage import upload_pictures, upload_models
from domino.models import *
from domino.db import Base, engine

Base.metadata.drop_all(engine, checkfirst=True)
Base.metadata.create_all(engine)

uploader = Uploader(
    {
        'pictures': 'domino_pictures.json',
        'ml_models': 'ml_objects.json'
    },
    {
        'pictures': upload_pictures,
        'ml_models': upload_models
    }
)
uploader.upload()
uploader.log()
uploader.print_message()