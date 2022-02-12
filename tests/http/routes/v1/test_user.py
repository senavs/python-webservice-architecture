from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.http.app import create_app
from app.src.schemas.user import UserModelSchema

app = TestClient(create_app())


def test_search_user_username_success(mocker: MockerFixture):
    # arrange
    user = {'id_user': 1, 'username': 'tester', 'email': 'tester@test.com'}
    mocker.patch("app.http.routes.v1.user.search_user_by_username", return_value=user)

    # act
    resp = app.get("/v1/users/", params={'username': user['username']})
    body = resp.json()

    # assert
    assert resp.status_code == 200
    assert body['idUser'] == user['id_user']
    assert body['username'] == user['username']
    assert body['email'] == user['email']


def test_search_user_email_success(mocker: MockerFixture):
    # arrange
    user = {'id_user': 1, 'username': 'tester', 'email': 'tester@test.com'}
    mocker.patch("app.http.routes.v1.user.search_user_by_email", return_value=user)

    # act
    resp = app.get("/v1/users/", params={'email': user['email']})
    body = resp.json()

    # assert
    assert resp.status_code == 200
    assert body['idUser'] == user['id_user']
    assert body['username'] == user['username']
    assert body['email'] == user['email']


def test_create_user_success(mocker: MockerFixture):
    # arrange
    user = {'id_user': 1, 'username': 'tester', 'email': 'tester@test.com'}
    mocker.patch("app.http.routes.v1.user.create_user", return_value=user)

    # act
    resp = app.post("/v1/users/", json=user)
    body = resp.json()

    # assert
    assert resp.status_code == 200
    assert body['idUser'] == user['id_user']
    assert body['username'] == user['username']
    assert body['email'] == user['email']


def test_update_user_success(mocker: MockerFixture):
    # arrange
    user = {'id_user': 1, 'username': 'tester', 'newEmail': 'new@test.com', 'email': 'tester@test.com'}
    mocker.patch("app.http.routes.v1.user.update_user_email", return_value=user)

    # act
    resp = app.put("/v1/users/", json=user)
    body = resp.json()

    # assert
    assert resp.status_code == 200
    assert body['idUser'] == user['id_user']
    assert body['username'] == user['username']
    assert body['email'] == user['email']
