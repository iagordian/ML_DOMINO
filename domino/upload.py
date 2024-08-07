
from upload import Uploader, upload_pictures
from models import *
from db import Base, engine

Base.metadata.drop_all(engine, checkfirst=True)
Base.metadata.create_all(engine)

uploader = Uploader(
    {
        'pictures': 'domino_pictures.json'
    },
    {
        'pictures': upload_pictures
    }
)
uploader.upload()
uploader.log()
uploader.print_message()