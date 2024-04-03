# -*- coding: utf-8 -*-

import multiprocessing
import os

from distutils.util import strtobool

os.getenv("GEMINI_API_KEY")

chdir = "src"

bind = os.getenv("WEB_BIND", "0.0.0.0:8000")
access_log = "-"
access_log_format = (
    "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"
)

workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))
threads = int(os.getenv("PYTHON_MAX_THREADS", 1))

reload = bool(strtobool(os.getenv("WEB_RELOAD", "false")))
