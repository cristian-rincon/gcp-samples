import json
from http import HTTPStatus


class TestHello:

    ENDPOINT = "/hello"

    def test_hello(self, client):
        response = client.get(self.ENDPOINT)
        assert response.status_code == HTTPStatus.OK

    def test_hello_response(self, client):
        response = client.get(self.ENDPOINT)
        response_decoded = json.loads(response.data.decode("utf-8"))
        assert response_decoded == {"hello": "App Engine Standard"}
