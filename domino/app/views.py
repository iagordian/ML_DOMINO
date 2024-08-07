
from fastapi import Request
from fastapi.responses import JSONResponse, StreamingResponse

from .app import app, templates
from schemas import Domino
from db import get_all_pictures, get_empty_picture, get_all_ML_logs
from ML import DominoClassificator
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

    if False:
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

    return JSONResponse({
        'status': 'ok'
    })

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