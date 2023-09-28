.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	apt update
	apt install python3-pip -y
	pip install pipenv==2023.9.8

python-packages:
	pipenv install

install: system-packages python-packages

tests:
	python manage.py test

run:
	python manage.py run

all: clean install tests run
