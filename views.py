import json
from flask import redirect, url_for
from flask.ext.restful import abort
from pony import orm
from app import app
from models import Page


def forward_endpoint(endpoint):
    redirect(url_for(endpoint))

@app.route('/')
def index():
    return "Welcome! Grab a seat!"

@app.route('/rest')
@app.route('/rest/<path:path>')
def rest(path=''):
    with orm.db_session():
        page = Page.get(path=path)
        if page:
            return '<html><body><pre>' + json.dumps(page.to_dict(), indent=2) + '</pre></body></html>'
        else:
            abort(404)
