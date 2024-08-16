
from fastapi import Request
from fastapi.responses import JSONResponse, StreamingResponse

from .app import app, templates
from schemas import Domino, PictureAnswer
from db import get_all_pictures, get_empty_picture, get_all_ML_logs, \
    get_img_bytes
from ML import DominoClassificator, DominoDecisionTree
import json
import io

@app.get('/')
async def index(request: Request):
    pictures = get_all_pictures()
    empty_picture = get_empty_picture()
    return templates.TemplateResponse('base.html', {'request': request,
                                                             'pictures': pictures,
                                                             'empty_picture': empty_picture})

@app.post('/ordered_check')
async def order_check(domino: Domino):

    if DominoDecisionTree.open().ordered_check(domino):
        ordered_check_decision = 2

    elif DominoClassificator.open().order_check(domino):
        ordered_check_decision = 1

    else:
        ordered_check_decision = 0

    return JSONResponse({
        'ordered_check': ordered_check_decision
    })


@app.post('/predict')
async def predict(domino: Domino):

    predicted_up, predicted_down = DominoDecisionTree.open().predict(domino)
    img_bytes = get_img_bytes(predicted_up, predicted_down)

    picture_answer = PictureAnswer(
        up=predicted_up,
        down=predicted_down,
        img=img_bytes
    )    

    return picture_answer

@app.get('/get_logs')
def get_logs():

    logs = get_all_ML_logs()

    img_container = io.StringIO()
    json.dump(logs, img_container, ensure_ascii=False, indent=4)
    img_container.seek(0)

    headers = {
        'Content-Disposition': 'attachment; filename="ML_logs.json"'
    }

    return StreamingResponse(img_container, headers=headers)