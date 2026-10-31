from conftest import client


def test_read_main(client):
    url = "/"
    response = client.get(url = url)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_user(client):
    url = "/users/create"
    params = {
        "user_name": "Alex"
    }
    response = client.post(url = url, params = params)

    assert response.status_code == 201
    assert response.json() == {"status": "ok"}
    # ------------------------------------------------------
    params_1 = {
        "user_name": "Andrew"
    }
    response_1 = client.post(url = url, params = params_1)

    assert response_1.status_code == 201
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
    response = client.post(url = "/users/create", params = {"user_name": "user to delete"})

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
    url = "/users/edit/rename"
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
                "id": 2,
                "name": "Andrew"
            },
            {
            "id": 1,
            "name": "AlexNew"
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
        "task_name": "Make the meal"
    }
    response_1 = client.post(url = url, params = params_1)
    assert response_1.status_code == 200
    assert response_1.json() == {"status": "ok"}

def test_get_tasks(client):
    url = "/tasks"
    response = client.get(url = url)
    assert response.status_code == 200
    assert response.json() == {
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


# Backend error (Model)
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
                "id": 2,
                "name": "Make the meal"
            },
            {
            "id": 1,
            "name": "Make videos"
            }
        ]
    }

    params_2 = {
        "task_id":   1,
        "task_name": "Make video"
    }
    response_2 = client.patch(url = url, params = params_2)
    assert response_2.status_code == 200
    assert response_2.json() == {"status": "ok"}

# Backend error (Model)
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
    assert response_1.json() == {
          "status": "ok",
          "message": [
            {
              "id": 2,
              "name": "Make the meal"
            },
            {
              "id": 1,
              "name": "Make video"
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
    assert response_1.status_code == 200
    assert response_1.json() == {"status": "ok"}

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

def test_end_tests(client):
    # Check start position
    users = {"status": "ok","message": [{"id": 2,"name": "Andrew"},{"id": 1,"name": "Alex"}]}
    tasks = {"status": "ok","message": [{"id": 2,"name": "Make the meal"},{"id": 1,"name": "Make video"}]}
    get_users_url = "/users"
    get_users_response = client.get(url=get_users_url)
    get_tasks_url = "/tasks"
    get_tasks_response = client.get(url=get_tasks_url)
    assert get_users_response.status_code == 200
    assert get_users_response.json() == users
    assert get_tasks_response.status_code == 200
    assert get_tasks_response.json() == tasks

    # Deleting all
    delete_user_url = "/users/delete"
    params_1 = {
        "user_id": 1
    }
    params_2 = {
        "user_id": 2
    }
    delete_user_response_1 = client.delete(url=delete_user_url, params=params_1)
    delete_user_response_2 = client.delete(url=delete_user_url, params=params_2)
    assert delete_user_response_1.status_code == 200
    assert delete_user_response_1.json() == {"status": "ok"}
    assert delete_user_response_2.status_code == 200
    assert delete_user_response_2.json() == {"status": "ok"}


    delete_task_url = "/tasks/delete"
    params_1 = {
        "task_id": 1
    }
    params_2 = {
        "task_id": 2
    }
    delete_task_response_1 = client.delete(url=delete_task_url, params=params_1)
    delete_task_response_2 = client.delete(url=delete_task_url, params=params_2)
    assert delete_task_response_1.status_code == 200
    assert delete_task_response_1.json() == {"status": "ok"}
    assert delete_task_response_2.status_code == 200
    assert delete_task_response_2.json() == {"status": "ok"}

    # Check delete operations
    general_response = {"status": "ok",  "message": []}
    get_users_url = "/users"
    get_users_response = client.get(url=get_users_url)
    get_tasks_url = "/tasks"
    get_tasks_response = client.get(url=get_tasks_url)
    assert get_users_response.status_code == 200
    assert get_users_response.json() == general_response
    assert get_tasks_response.status_code == 200
    assert get_tasks_response.json() == general_response
