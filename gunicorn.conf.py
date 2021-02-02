import os
import multiprocessing


HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", "5000")
ENV = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "False")

bind = f"{HOST}:{PORT}"
workers = multiprocessing.cpu_count() * 2 + 1
# we might need to change worker_class to something better handling I/O database operations, possibly gevent
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

daemon = False
proc_name = "party_wall_django"

loglevel = "debug" if DEBUG == "True" else "info"
# errorlog = ""
# accesslog = ""
# access_log_format = ""


if ENV in ["development", "dev"]:
    workers = 1
    reload = True
