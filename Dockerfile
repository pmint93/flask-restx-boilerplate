FROM python:3.7

ENV WORKDIR /app

WORKDIR $WORKDIR

RUN pip install pipenv==2023.9.8

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy --system

COPY . .

CMD ["gunicorn", "-c", "gunicorn.py", "wsgi:app"]
