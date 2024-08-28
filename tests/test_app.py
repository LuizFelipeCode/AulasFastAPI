from http import HTTPStatus

from fastapi.testclient import TestClient

from estudo_fast.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)    # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK    # assert
    assert response.json() == {'message': 'Olá Mundo!'}     # assert
