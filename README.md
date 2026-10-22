# [CLI] Team task manager (self-edu project)
#### Manage your team's tasks in light simple-using task manager
####
###### Project idea by [avito-tech/tech-internship](https://github.com/avito-tech/tech-internship)

## Techs
- Python 3.11
  - FastAPI
  - SQLAlchemy
- Docker
- PostgreSQL 17

## Installation

- ### Build & Launch
```
docker compose -f .\docker\docker-compose.yaml up --build -d
```

- ###### Rebuild (Drop DB and re-install)
~~~
docker compose -f .\docker\docker-compose.yaml down -v
~~~
___
- ###### Using
  - ###### Logs
  ~~~
  docker compose -f .\docker\docker-compose.yaml logs -f
  ~~~
___
### TODO:
- Tests
- Update/upgrade README.md