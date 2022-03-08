# Ferment Pi



## Database
Navigate to `db/`

To create the image for the db run:
```
$ docker build -t fermentpi_db . --build-arg REGISTRY=docker.io/library
```
Then navigate back to the root directory and run:
```
$ docker-compose up
```

To run the migration run
```
$ python ./src/ferment_pi/pre_start.py
```


## Frontend

Navigate to `frontend/ferment-pi`

Install the dependencies

```
$ yarn install
```

### Run 
To run the dev version, run
```
$ yarn start
```

### Test
To run the frontend unit-tests
```
$ yarn test
```

### Build

To build run
```
$ yarn build
```

## Server

Install the dependencies

```
$ pipenv install --dev
```

Activate the virtual environment

```
$ pipenv shell
```

### Testing
To run the backend unit-tests run:
```
$ pytest
```
_(single run)_
or

```
$ ptw
```
_(watcher)_

### Running

_(note:)_ To run the server, you need to build the frontend first

To run the FastAPI server, run
```
$ ./scripts/run_server.sh
```

