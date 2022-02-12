from fastapi import FastAPI
from pytest_mock import MockerFixture

from app.http.app import create_app


def test_create_app(mocker: MockerFixture):
    # arrange
    register_errors_handler = mocker.patch('app.http.app.register_errors_handler')
    register_middlewares = mocker.patch('app.http.app.register_middlewares')
    register_routes = mocker.patch('app.http.app.register_routes')

    # act
    app = create_app()

    # assert
    assert isinstance(app, FastAPI)
    register_errors_handler.assert_called_once()
    register_middlewares.assert_called_once()
    register_routes.assert_called_once()
