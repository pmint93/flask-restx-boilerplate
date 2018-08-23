# Flask-Restplus Boilerplate

## Development

### Make commands

Initial installation: make install

To run test: make tests

To run application: make run

To run all above commands at once: make all

### Other commands

To open an interactive shell: python manage.py shell

See supported commands: python manage.py --help

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
$ git clone <repo-url> /opt/<app-name>
$ cd /opt/<app-name>/
$ virtualenv --python=${python_version} .
$ source bin/activate
$ pip install -r requirements.txt
```

Copy and **modify** example environment config

```bash
$ cp /opt/<app-name>/.env.production.tpl /opt/<app-name>/.env.production
$ nano /opt/<app-name>/.env.production
```

Install systemd service

```bash
$ cp /opt/<app-name>/<app-name>.service /etc/systemd/system/<app-name>.service
```

Install rsyslog config

```bash
$ cp /opt/<app-name>/<app-name>.rsyslog.conf /etc/rsyslog.d/<app-name>.conf
```

Restart rsyslog

```bash
$ systemctl restart rsyslog
```

Enable service to run on boot

```bash
$ systemctl enable <app-name>
```

Start service

```bash
$ service <app-name> start
```

Verify service start successfully

```bash
$ service <app-name> status
```

Service log available in `journalctl -u <app-name>` and `/var/log/<app-name>.log`

### Running on docker container

Build image, and run as normal

See example environment config in [.env.production.tpl](./.env.production.tpl)

See available configuration in [config.py](./app/main/config.py) and [gunicorn.conf](./gunicorn.conf)
