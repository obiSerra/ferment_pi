#!/bin/bash

read -p "Truncate temperatures table? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    docker exec -it fermentpi_fermentpi_db_service_1 psql -U testuser -d fermentpi_db -c "TRUNCATE temperatures"
fi



