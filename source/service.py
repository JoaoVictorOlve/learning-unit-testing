
import requests
import mock
import source.service as service
import pytest

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError

@mock.patch("request.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id:":1, "name":"Jefferson"}
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id:":1, "name":"Jefferson"}

@mock.patch("request.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
    