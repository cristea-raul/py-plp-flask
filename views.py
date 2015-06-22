import json
from flask import redirect, url_for, render_template
from pony import orm
from app import app
from models import Page

def _temp_json_printer(json_str):
    ret = '<html><body><pre>'
    ret += json_str
    ret += '</pre></body></html>'

def forward_endpoint(endpoint):
    redirect(url_for(endpoint))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rest')
@app.route('/rest/<path:path>')
def rest(path=''):
    with orm.db_session():
        page = Page.get(path=path)
        if page:
            return _temp_json_printer(json.dumps(page.to_dict(), indent=2))
        else:
            return 'Not Found', 404
