# Forgerock Technical Challenge

# Setup
## Local
1. Setup `venv`.
```
$ python -m venv env
```
2. Activate `venv`.
```
$ source env/bin/activate
```
3. Install required pip packages.
```
$ pip3 install -r requirements.txt
```
4. Launch app locally.
```
$ python server.py
```

## Docker
1. Run docker-compose.
```
$ docker-compose run --rm --service-ports forgerock-challenge-app
```
2. By default, app is now listening on `http://0.0.0.0:5000`. On a separate terminal, try query the API endpoint.
```
$ curl http://localhost:5000/
```
