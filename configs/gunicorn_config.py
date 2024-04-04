# -*- coding: utf-8 -*-

import multiprocessing

chdir = "src"


bind = "0.0.0.0:8000"
backlog = 2048


workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
worker_connections = 1000

timeout = 300
keepalive = 2
