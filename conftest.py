import pytest

@pytest.fixture(scope="session")
def browser():
    print("Бrowser!!")

    yield

    print("Сезам, закройся, браузер")