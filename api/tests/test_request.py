# import falcon
# from falcon import testing
# import pytest
#
# from api.app import api
#
#
# @pytest.fixture
# def client():
#     return testing.TestClient(api)
#
#
# # pytest will inject the object returned by the "client" function
# # as an additional parameter.
# def test_request(client):
#     response = client.simulate_get('/request')
#     # result_doc = msgpack.unpackb(response.content, encoding='utf-8')
#
#     # assert result_doc == doc
#     assert response.status == falcon.HTTP_OK