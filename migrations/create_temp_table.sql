CREATE TABLE temperatures (
    id SERIAL NOT NULL,
    temperature int NOT NULL,
    humidity int NOT NULL,
    created_time timestamp NOT NULL,
    PRIMARY KEY (id)
);