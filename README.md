# Ferment Pi



## Database

The db can be started with the 
```
$ docker-compose up
```

## Frontend

Navigate to `frontend/`

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

