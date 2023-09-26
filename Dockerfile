FROM python:3.7

ENV INSTALL_PATH /app

WORKDIR $INSTALL_PATH

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-c", "gunicorn.conf", "wsgi:app"]
