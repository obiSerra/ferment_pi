#!/bin/bash

docker exec -it fermentpi_fermentpi_db_service_1 psql -U testuser -d fermentpi_db -c "$(cat ../queries/create_temp_table.sql)"