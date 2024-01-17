# -*- coding: utf-8 -*-

import multiprocessing

bind = "0.0.0.0:8000"

# workers = multiprocessing.cpu_count() * 2 + 1
workers = 4

max_requests = 1000
max_requests_jitter = 50

timeout = 300

accesslog = "logs/access.log"
errorlog = "logs/error.log"
loglevel = "info"
