from conftest import client


def test_read_main(client):
    url = "/"
    response = client.get(url = url)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_user(client):
    url = "/"
    params = {
        "user_name": "Alex"
    }
    response = client.get(url = url, params = params)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    # ------------------------------------------------------
    params_1 = {
        "user_name": "Andrew"
    }
    response_1 = client.post(url = url, params = params_1)

    assert response_1.status_code == 200
    assert response_1.json() == {"status": "ok"}

def test_get_users(client):
    url = "/users"
    response = client.get(url = url)

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": [
            {
                "id": 1,
                "name": "Alex"
            },
            {
            "id": 2,
            "name": "Andrew"
            }
        ]
    }

def test_delete_user(client):
    response = client.post(url = "/", params = {"user_name": "user to delete"})

    url = "/users/delete"
    params = {
        "user_id": 3
    }
    response = client.delete(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    url_1 = "/users"
    response_1 = client.get(url = url_1)

    assert response_1.status_code == 200
    assert response_1.json() == {
            "status": "ok",
            "message": [
                {
                    "id": 1,
                    "name": "Alex"
                },
                {
                "id": 2,
                "name": "Andrew"
                }
            ]
        }

def test_get_user(client):
    url = "/users/get"
    params = {
        "user_id": 1
    }
    response = client.get(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {
            "status": "ok",
            "message": {
                "id": 1,
                "name": "Alex"
            }
        }

def test_rename_user(client):
    url = "/users/rename"
    params = {
        "user_id":   1,
        "user_name": "AlexNew"
    }
    response = client.patch(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    url_1 = "/users"
    response_1 = client.get(url = url_1)
    assert response_1.status_code == 200
    assert response_1.json() == {
        "status": "ok",
        "message": [
            {
                "id": 1,
                "name": "AlexNew"
            },
            {
            "id": 2,
            "name": "Andrew"
            }
        ]
    }

    params_2 = {
        "user_id":   1,
        "user_name": "Alex"
    }
    response_2 = client.patch(url = url, params = params_2)
    assert response_2.status_code == 200
    assert response_2.json() == {"status": "ok"}


def test_create_task(client):
    url = "/tasks/create"
    params = {
        "task_name": "Make video"
    }
    response = client.post(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    # ------------------------------------------------------
    params_1 = {
        "user_name": "Make the meal"
    }
    response_1 = client.post(url = url, params = params_1)
    assert response_1.status_code == 200
    assert response_1.json() == {"status": "ok"}

def test_get_tasks(client):
    url = "/tasks"
    response = client.get(url = url)
    assert response.status_code == 200
    assert response.json == {
          "status": "ok",
          "message": [
            {
              "id": 1,
              "name": "Make video"
            },
            {
              "id": 2,
              "name": "Make the meal"
            }
          ]
        }

def test_rename_task(client):
    url = "/tasks/edit/rename"
    params = {
        "task_id":   1,
        "task_name": "Make videos"
    }
    response = client.patch(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    url_1 = "/tasks"
    response_1 = client.get(url = url_1)
    assert response_1.status_code == 200
    assert response_1.json() == {
        "status": "ok",
        "message": [
            {
                "id": 1,
                "name": "Make videos"
            },
            {
            "id": 2,
            "name": "Make the meal"
            }
        ]
    }

    params_2 = {
        "user_id":   1,
        "user_name": "Make video"
    }
    response_2 = client.patch(url = url, params = params_2)
    assert response_2.status_code == 200
    assert response_2.json() == {"status": "ok"}

def test_delete_task(client):
    url_1 = "/tasks/create"
    params_1 = {
        "task_name": "Task to delete"
    }
    response = client.post(url = url_1, params = params_1)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    url = "/tasks/delete"
    params = {
        "task_id": 3
    }
    response = client.delete(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}



    url_1 = "/tasks"
    response_1 = client.get(url = url_1)
    assert response_1.status_code == 200
    assert response_1.json == {
          "status": "ok",
          "message": [
            {
              "id": 1,
              "name": "Make video"
            },
            {
              "id": 2,
              "name": "Make the meal"
            }
          ]
        }

def test_add_user2task_AND_get_users_by_task(client):
    url = "/tasks/edit/users/add"
    params = {
        "user_id": 1,
        "task_id": 1
    }
    response = client.patch(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    url_1 = "/tasks/users"
    params_1 = {
        "task_id": 1
    }
    response_1 = client.get(url = url_1, params = params_1)
    assert response.status_code == 200
    assert response.json() == {
            "status": "ok",
            "message": [
            {
              "id": 1,
              "name": "Alex"
            }
            ]
        }

def test_get_tasks_by_user(client):
    url = "/users/tasks"
    params = {
        "user_id": 1
    }
    response = client.get(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {
          "status": "ok",
          "message": [
            {
              "id": 1,
              "name": "Make video"
            }
          ]
        }

def test_remove_user_from_task(client):
    url = "/tasks/edit/users/remove"
    params = {
        "user_id": 1,
        "task_id": 1
    }
    response = client.patch(url = url, params = params)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
