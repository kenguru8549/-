import pytest
from project.pages.login_page import LoginPage
from project.pages.dashboard_page import DashboardPage

  #  Фикстуры login_page и dashboard_page используются для инициализации соответствующих объектов.
@pytest.fixture  #  фикстуры создают экземпляры LoginPage и DashboardPage, которые могут быть использованы в тестах
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
