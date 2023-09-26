FROM python:3.7

ENV WORKDIR /app

WORKDIR $WORKDIR

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-c", "gunicorn.py", "wsgi:app"]
