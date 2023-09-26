FROM python:3.7

ENV WORKDIR /app

WORKDIR $WORKDIR

RUN pip install pipenv==2023.9.8

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-c", "gunicorn.py", "wsgi:app"]
