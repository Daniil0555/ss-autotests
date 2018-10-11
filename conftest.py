import pytest
from fixture.application import Aplication


@pytest.fixture(scope="session")  # scope - что бы не перезапускать браузер для каждого теста / фикстура создается один раз и все тесты ее используют
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture

#dsfasdfasdfasdfasdf
