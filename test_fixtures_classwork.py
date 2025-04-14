import pytest

@pytest.fixture
def login_page(browser):
    print("Логин")
    pass

@pytest.fixture
def user():
    print("Юзверь!")
    return "username", "password"

def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"

def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"