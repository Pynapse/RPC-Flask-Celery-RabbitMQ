help:
	@echo "    clean-pyc"
	@echo "        Delete python temp files"
	@echo "    isvirtualenv"
	@echo "        Check virtualenv"
	@echo "    dep"
	@echo "        Install dependencies from requirements.txt"
	@echo "    pylint"
	@echo "        Code check with pylint"
	@echo "    create_venv"
	@echo "        Create virtual environment with py3.6"
	@echo "    run-devserver"
	@echo "        Run Flask at 0.0.0.0:5000"
	@echo "    run-gunicorn"
	@echo "        Run flask with gunicorn"
	@echo "    python_v"
	@echo "        Python version in current environment"


clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +

run-gunicorn:
	celery -A rest_app.celery worker --loglevel=info & gunicorn -c gunicorn.config.py rest_app:app

run-devserver:
	celery -A rest_app.celery worker --loglevel=info & python -m rest_app

pylint:
	pylint rest_app.py

create_venv:
	mkdir $(PWD)/venv && cd $(PWD)/venv; \
	python3 -m venv project_env; \

isvirtualenv:
	@if [ -z "$(VIRTUAL_ENV)" ]; then echo "ERROR: Not in a virtualenv. Need to 'source venv/project_env/bin/activate'" 1>&2; exit 1; fi

dep:
	make isvirtualenv;
	pip install -r requirements.txt

python_v:
	python --version

pep8_autoformat:
	autopep8 --in-place --aggressive --aggressive rest_app.py; \
	autopep8 --in-place --aggressive --aggressive reg_tasks/active_tasks.py; \
	autopep8 --in-place --aggressive --aggressive celery_obj/celery1.py; \

