# -*- coding: utf-8 -*-

import multiprocessing
import os

from distutils.util import strtobool

chdir = "src"

bind = os.getenv("WEB_BIND", "0.0.0.0:8000")

access_log = "-"
access_log_format = (
    "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"
)

worker_class = "gevent"
worker_connections = 1000
workers = 3

reload = bool(strtobool(os.getenv("WEB_RELOAD", "false")))
