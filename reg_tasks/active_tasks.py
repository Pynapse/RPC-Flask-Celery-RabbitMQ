from __future__ import absolute_import
from flask import Flask, request, jsonify
import time
import urllib.request
import json
from celery import Celery, uuid
from bs4 import BeautifulSoup
from collections import defaultdict
from celery.task.control import inspect
from celery_obj.celery1 import celery

celery.conf.CELERY_ACCEPT_CONTENT = ['json']
celery.conf.CELERY_TASK_SERIALIZER = 'json'
celery.conf.CELERY_RESULT_SERIALIZER = 'json'
celery.conf.BROKER_POOL_LIMIT = 1000

@celery.task
def url_to_data(url):
    time.sleep(5)
    d = defaultdict(int)
    url = urllib.request.urlopen(url)
    s = url.read()
    sp = BeautifulSoup(s.decode("utf8"))
    for tag in sp.findAll():
        d[tag.name] += 1
    return d
