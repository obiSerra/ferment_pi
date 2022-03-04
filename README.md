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

### Build

To build run
```
$ yarn build
```

## Server

Install the dependencies

```
$ pipenv install
```

Activate the virtual environment

```
$ pipenv shell
```

### Running

(note) To run the server, you need to build the frontend first

To run the FastAPI server, run
```
$ ./scripts/run_server.sh
```

