from conftest import client


def test_read_main(client):
    url = "/"
    response = client.get(url = url)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_user(client):
    url = "/"
    params = {
        "user_name": "Test User"
    }
    response = client.get(url = url, params = params)

    assert response.status_code == 200
