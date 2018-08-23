# Flask-Restplus Boilerplate

## Development

### Make commands

Initial installation: `make install`

To run test: `make tests`

To run application: `make run`

To run all above commands at once: `make all`

### Other commands

To open an interactive shell: `python manage.py shell`

See supported commands: `python manage.py --help`

### Viewing the app ###

Open the following url on your browser to view swagger documentation
http://127.0.0.1:5000/

## Production

### Running on Linux distributions

#### Prerequisites

1. [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

#### Installation

```bash
$ python_version=python3.6
$ git clone <repo-url> /opt/flask-restplus-boilerplate
$ cd /opt/flask-restplus-boilerplate/
$ virtualenv --python=${python_version} .
$ source bin/activate
$ pip install -r requirements.txt
```

Copy and **modify** example environment config

```bash
$ cp /opt/flask-restplus-boilerplate/.env.production.tpl /opt/flask-restplus-boilerplate/.env.production
$ nano /opt/flask-restplus-boilerplate/.env.production
```

Install systemd service

```bash
$ cp /opt/flask-restplus-boilerplate/flask-restplus-boilerplate.service /etc/systemd/system/flask-restplus-boilerplate.service
```

Install rsyslog config

```bash
$ cp /opt/flask-restplus-boilerplate/flask-restplus-boilerplate.rsyslog.conf /etc/rsyslog.d/flask-restplus-boilerplate.conf
```

Restart rsyslog

```bash
$ systemctl restart rsyslog
```

Enable service to run on boot

```bash
$ systemctl enable flask-restplus-boilerplate
```

Start service

```bash
$ service flask-restplus-boilerplate start
```

Verify service start successfully

```bash
$ service flask-restplus-boilerplate status
```

Service log available in `journalctl -u flask-restplus-boilerplate` and `/var/log/flask-restplus-boilerplate.log`

### Running on docker container

Build image, and run as normal

See example environment config in [.env.production.tpl](./.env.production.tpl)

See available configuration in [config.py](./app/main/config.py) and [gunicorn.conf](./gunicorn.conf)
