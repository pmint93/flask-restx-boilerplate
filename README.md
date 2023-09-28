# Flask-Restx Boilerplate

## Local development

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

## Deploy

### Running on Linux distributions

#### Prerequisites

1. [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

#### Installation

```bash
$ python_version=python3.7
$ git clone <repo-url> /opt/flask-restx-boilerplate
$ cd /opt/flask-restx-boilerplate/
$ virtualenv --python=${python_version} .
$ source bin/activate
$ pip install -r requirements.txt
```

Copy and **modify** example environment config

```bash
$ cp /opt/flask-restx-boilerplate/.env.deploy.tpl /opt/flask-restx-boilerplate/.env.deploy
$ nano /opt/flask-restx-boilerplate/.env.deploy
```

Install systemd service

```bash
$ cp /opt/flask-restx-boilerplate/flask-restx-boilerplate.service /etc/systemd/system/flask-restx-boilerplate.service
```

Install rsyslog config

```bash
$ cp /opt/flask-restx-boilerplate/flask-restx-boilerplate.rsyslog.conf /etc/rsyslog.d/flask-restx-boilerplate.conf
```

Restart rsyslog

```bash
$ systemctl restart rsyslog
```

Enable service to run on boot

```bash
$ systemctl enable flask-restx-boilerplate
```

Start service

```bash
$ service flask-restx-boilerplate start
```

Verify service start successfully

```bash
$ service flask-restx-boilerplate status
```

Service log available in `journalctl -u flask-restx-boilerplate` and `/var/log/flask-restx-boilerplate.log`

### Running on docker container

Build image, and run as normal

See example environment config in [.env.deploy.tpl](./.env.deploy.tpl)

See available configuration in [config.py](./app/main/config.py) and [gunicorn.conf](./gunicorn.conf)
