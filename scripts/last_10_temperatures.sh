#!/bin/bash

docker exec -it fermentpi_fermentpi_db_service_1 psql -U testuser -d fermentpi_db -c "SELECT * FROM temperatures ORDER BY created_time DESC LIMIT 10"

