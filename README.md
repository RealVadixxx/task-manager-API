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
docker compose up --build -d
```

- ###### Rebuild (Drop DB and re-install)
~~~
docker compose down -v  
~~~
___
### TODO:
- Make command-line interface
  - Main menu (home)
    - Tasks with connected users
  - Task manager
    - Create / Remove / Manage (add/remove user) task
  - User manager
    - Create / Remove / Manage (add/remove task) user
  
- Tests
- Update/upgrade README.md