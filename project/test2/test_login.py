import pytest
from project.pages.login_page import LoginPage
  # переместили в конфтест from pages.login_page import LoginPage
  # переместили в конфтест from pages.dashboard_page import DashboardPage
def test_login_failure(page):  #  функция проверяет то ли сообщение об ошибке появляется на странице Логин
    # переместили в конфтест login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('invalid_user', 'invalid_password')
    assert login_page.url == 'https://zimaev.github.io/pom/'  #  проверка, что урл не изменился
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'  #  проверка, что сообщение именно такое

def test_login_success(page):  #  Проверяется, что на странице отображается корректное приветственное сообщение
    # переместили в контест login_page = LoginPage(page)
    # переместили в контест dashboard_page = DashboardPage(page)
    login_page.navigate()
    login_page.login('admin', 'admin')

    dashboard_page.assert_welcome_message("Welcome admin")


@pytest.mark.parametrize('username, password', [  #  функция с параметризацией, исполнится для каждой пары логина и пароля
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(page, username, password):
    # переместили в контест login_page = LoginPage(page)
    # переместили в контест dashboard_page = DashboardPage(page)
    login_page.navigate()
    login_page.login(username, password)

    dashboard_page.assert_welcome_message(f"Welcome {username}")