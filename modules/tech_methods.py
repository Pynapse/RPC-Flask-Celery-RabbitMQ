from __future__ import absolute_import
from flask import Flask, request
import sys, errno

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def shutdown_gunicorn():
    sys.exit(4)
