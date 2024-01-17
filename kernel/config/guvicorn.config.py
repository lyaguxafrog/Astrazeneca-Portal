# -*- coding: utf-8 -*-

import multiprocessing

bind = "127.0.0.1:8000"

workers = multiprocessing.cpu_count() * 2 + 1

max_requests = 1000
max_requests_jitter = 50

timeout = 30

accesslog = "logs/access.log"
errorlog = "logs/error.log"
loglevel = "info"
