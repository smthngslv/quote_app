import json
from random import choice

from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title='QuoteApp',
    version='1.0.0'
)

app.mount(
    '/static',
    StaticFiles(directory='./quote/static')
)

# Load quotes.
with open('./quote/data.json') as file:
    quotes = json.load(file)['quotes']


@app.get('/quote', response_class=JSONResponse)
def quote() -> dict:
    return choice(quotes)


@app.get('/', response_class=RedirectResponse)
def main() -> RedirectResponse:
    return RedirectResponse('/static/index.html')
