# Forgerock Technical Challenge

## Setup
### Local
1. Setup `venv`
```
$ python -m venv env
```
2. Activate `venv`
```
$ source env/bin/activate
```
3. Install required pip packages
```
$ pip3 install -r requirements.txt
```
### Docker
Run docker-compose.
```
$ docker-compose run --rm --service-ports forgerock-challenge-app
```
