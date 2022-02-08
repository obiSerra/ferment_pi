#!/bin/sh

echo "[+] Building fermentpi_db"
cd "./db"
docker build -t fermentpi_db . --build-arg REGISTRY=docker.io/library

cd ".."
echo "[+] Starting compose"