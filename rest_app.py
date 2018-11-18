from __future__ import absolute_import
#import time
#import urllib
import json
#from celery import Celery, uuid
#from bs4 import BeautifulSoup
#from collections import defaultdict

#from celery import Celery, uuid
from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, request, jsonify
from celery_obj.celery1 import celery
from reg_tasks.active_tasks import url_to_data
from modules.tech_methods import shutdown_server  # for 127.0.0.1:5000 dev server
from modules.tech_methods import shutdown_gunicorn

app = Flask(__name__)

@app.route('/tags', methods=['POST', 'GET'])
def calculatetags():
    if request.method == "POST":
        print(json.loads(request.data)['url'])
        task = url_to_data.apply_async(args=[json.loads(request.data)['url']])
        r = task.id
    if request.method == "GET":
        print(request.args.get('taskn'))
        task = url_to_data.AsyncResult(request.args.get('taskn'))
        if task.state == 'PENDING':
            response = {
                'state': task.state,
                'status': 'Pending...'
            }
        elif task.state != 'FAILURE':
            response = {
                'state': task.state,
                'status': task.info.get('status', ''),
                'result': task.result
            }
        else:
            # background errors
            response = {
                'state': task.state,
                'status': str(task.info),
            }
        r = jsonify(response)
    return r


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Process killed'


@app.route('/shutdown_g', methods=['POST'])
def shutdown_g():
    shutdown_gunicorn()
    return 'Process killed'


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
