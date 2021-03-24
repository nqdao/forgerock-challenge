# Forgerock Technical Challenge
Single integration test command with `docker-compose`
```
$ docker-compose run --rm forgerock-challenge-app python -m unittest discover -s tests -p "*.py"
```

# Setup
## Local Setup
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

## Docker Setup
1. Build Docker image.
```
$ docker build . -t forgerock-challenge:latest
```
2. Run Docker container.
```
$ docker run forge-challenge:latest
```

## Access App
3. By default, app is now listening on `http://0.0.0.0:5000`. On a separate terminal, try query the API endpoint.
```
$ curl http://localhost:5000/
```

# Testing
## Local Tests
1. Activate your `venv`
```
$ source env/bin/activate
```
2. Run unit tests
```
$ python -m unittest utils.py
```
3. Run integration tests
```
$ python -m unittest discover -s tests -p "*.py"
```

## Docker Tests
1. Run unit tests in Docker container.
```
$ docker run forgerock-challenge:latest python -m unittest utils.py
```
2.  Run tests in Docker container.
```
$ docker run forgerock-challenge:latest python -m unittest discover -s tests -p "*.py"
```
