from __future__ import absolute_import
from celery import Celery
#from celery_obj.celery_config.rabbitmq_conf import Rabbitmq_CONFIG

celery = Celery('rest_app',
                broker='amqp://kas:kas@rabbit/kas_vhost',
                backend='rpc://')
