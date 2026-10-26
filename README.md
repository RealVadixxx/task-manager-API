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

<details>
<summary><b>GET /users</b> — Получить пользователей</summary>

#### Параметры пути (URL)
* 

#### Пример успешного ответа (`200 OK`)
```json
{
  "status": "ok",
  "message": [
    {
      "id": 1,
      "name": "Alex"
    }
  ]
}
```

</details>

<details>
<summary><b>GET /users/tasks</b> — Получить задания пользователя</summary>

#### Параметры пути (URL)
* ```json
  "user_id" - ID пользователя 
  ```

#### Пример успешного ответа (`200 OK`)
```json
{
  "status": "ok",
  "message": [
    {
      "id": 1,
      "name": "Do homework"
    }
  ]
}
```

</details>
<details>
<summary><b>GET /users/get</b> — Получить информацию о пользователе</summary>

#### Параметры пути (URL)
* ```json
  "user_id" - ID пользователя
  ```

#### Пример успешного ответа (`200 OK`)
```json
{
  "status": "ok",
  "message": {
    "id": 1,
    "name": "Alex"
  }
}
```

</details>
<details>
<summary><b>POST /users/create</b> — Создать пользователя</summary>

#### Параметры пути (URL)
* ```json
  "user_name" - Имя пользователя
  ```

#### Пример успешного ответа (`200 OK`)
```json
{"status": "ok"}
```

</details>
<details>
<summary><b>PATCH /users/edit/rename</b> — Переименовать пользователя</summary>

#### Параметры пути (URL)
* ```json
  "user_id"   - ID пользователя
  "user_name" - Новое имя пользователя
  ```

#### Пример успешного ответа (`200 OK`)
```json
{"status": "ok"}
```

</details>
<details>
<summary><b>DELETE /users/delete</b> — Удалить пользователя</summary>

#### Параметры пути (URL)
* ```json
  "user_id" - ID пользователя
  ```

#### Пример успешного ответа (`200 OK`)
```json
{"status": "ok"}
```

</details>
<details>
<summary><b>GET /tasks</b> — Получить задания (сегменты)</summary>

#### Параметры пути (URL)
* 

#### Пример успешного ответа (`200 OK`)
```json
{
  "status": "ok",
  "message": [
    {
      "id": 1,
      "name": "Do homework"
    }
  ]
}
```

</details>
<details>
<summary><b>GET /tasks/users</b> — Получить пользователей в задании (сегменте)</summary>

#### Параметры пути (URL)
* ```json
  "task_id" - ID задания
  ```

#### Пример успешного ответа (`200 OK`)
```json
{
  "status": "ok",
  "message": [
    {
      "id": 1,
      "name": "Alex"
    }
  ]
}
```

</details>
<details>
<summary><b>GET /tasks/get</b> — Получить информацию о задании</summary>

#### Параметры пути (URL)
* ```json
  "task_id" - ID задания (сегмента)
  ```

#### Пример успешного ответа (`200 OK`)
```json
{
  "status": "ok",
  "message": {
    "id": 1,
    "name": "Do homework"
  }
}
```

</details>
<details>
<summary><b>POST /tasks/create</b> — Создать задание (сегмент)</summary>

#### Параметры пути (URL)
* ```json
  "task_name" - Имя задания (сегмента)
  ```

#### Пример успешного ответа (`200 OK`)
```json
{"status": "ok"}
```

</details>
<details>
<summary><b>PATCH /tasks/edit/rename</b> — Переименовать задание (сегмент)</summary>

#### Параметры пути (URL)
* ```json
  "task_id"   - ID задания (сегмента)
  "task_name" - Новое имя задания (сегмента)
  ```

#### Пример успешного ответа (`200 OK`)
```json
{"status": "ok"}
```

</details>
<details>
<summary><b>PATCH /tasks/edit/users/add</b> — Добавить пользователя в задание (сегмент)</summary>

#### Параметры пути (URL)
* ```json
  "task_id" - ID задания (сегмента)
  "user_id" - ID пользователя
  ```

#### Пример успешного ответа (`200 OK`)
```json
{"status": "ok"}
```

</details>
<details>
<summary><b>PATCH /tasks/edit/users/remove</b> — Убрать пользователя из задания (сегмента)</summary>

#### Параметры пути (URL)
* ```json
  "task_id" - ID задания (сегмента)
  "user_id" - ID пользователя
  ```

#### Пример успешного ответа (`200 OK`)
```json
{"status": "ok"}
```

</details>
<details>
<summary><b>DELETE /tasks/delete</b> — Удалить задание (сегмент)</summary>

#### Параметры пути (URL)
* ```json
  "task_id" - ID задания (сегмента)
  ```

#### Пример успешного ответа (`200 OK`)
```json
{"status": "ok"}
```

</details>
