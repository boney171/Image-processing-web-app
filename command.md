# Activate the virtual enviroment: venv/bin/
# start redis: brew services start redis
# stop redis: brew services stop redis
# restart : brew services restart redis
# set python path to acces backend common dir: export PYTHONPATH="/Users/treetran171/Workspace/webapp:$PYTHONPATH"
# start celery worker threads: celery -A mybackend worker -l info
# to watch celery -A worker logs: celery -A mybackend worker -l debug