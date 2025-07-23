"""Gunicorn config file"""

# The granularity of Error log outputs
loglevel = "debug"

# The number of worker processes for handling requests
workers = 1

# The socket to bind
bind = "127.0.0.1:8257"

# Restart workers when code changes (development only!)
reload = False

# Write access and error info to /var/log
errorlog =  "./gunicorn-error.log"
accesslog = "./gunicorn-access.log"

# Redirect stdout/stderr to log file
#capture_output = True
# PID file so you can easily fetch process ID
#pidfile = "/var/run/gunicorn/dev.pid"
