# Team task manager (self-edu project)
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

## Using
### Endpoints
 - GET /users
 - GET /users/tasks
 - GET /users/get 
 - POST /users/create
 - PATCH /users/edit/rename
 - DELETE /users/delete

 - GET /tasks
 - GET /tasks/users
 - GET /tasks/get
 - POST /tasks/create
 - PATCH /tasks/edit/rename
 - PATCH /tasks/edit/users/add
 - PATCH /tasks/edit/users/remove
 - DELETE /tasks/delete

~~~