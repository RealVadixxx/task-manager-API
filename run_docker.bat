@echo off

docker compose -f .\docker\docker-compose.yaml down -v

docker compose -f .\docker\docker-compose.yaml up --build -d

docker compose -f .\docker\docker-compose.yaml logs -f