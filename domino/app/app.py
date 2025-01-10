
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Callable
from domino.loger import url_query_log, server_error_log

templates = Jinja2Templates(directory='domino/templates')

app = FastAPI(title='Гранит')
app.mount("/static", StaticFiles(directory="domino/static"), name="static")

@app.exception_handler(Exception)
async def auth_exception_cautch(request: Request, exc: Exception):
    return server_error_log(request.__dict__['scope']['path'], exc)