# project/pages/login_page.py
from playwright.sync_api import Page

class LoginPage:  #  Конструктор класса — это метод __init__. Он вызывается при создании нового объекта этого класса. В нашем случае, он будет принимать объект страницы (page), который будет использоваться для взаимодействия с элементами веб-страницы
    def __init__(self, page: Page):  #  page: Page — это аннотация типа, указывающая, что параметр page должен быть объектом типа Page из Playwright
        self.page = page  #  сохраняет переданный объект страницы в атрибуте экземпляра класса для дальнейшего использования
        self.username_input = page.locator('#username')  #  Поле ввода имени пользователя:   у этого есть идентификатор #username
        self.password_input = page.locator('#password')  #  Поле ввода пароля: у этого элемента есть идентификатор #password
        self.login_button = page.locator('#login')  #  Кнопка входа:  у этого элемента есть идентификатор #login
        self.error_message = page.locator('#errorAlert')  #  Сообщение об ошибке: у этого элемента есть идентификатор #errorAlert

def navigate(self):  #  Метод navigate
   # """Открывает страницу логина."""
    self.page.goto('https://zimaev.github.io/pom/')

def login(self, username: str, password: str):  #  Метод login
  #  """Выполняет вход с заданными учетными данными."""
    self.username_input.fill(username)
    self.password_input.fill(password)
    self.login_button.click()

def get_error_message(self):  #  Метод get_error_message
    """Возвращает текст сообщения об ошибке."""
    return self.error_message.inner_text()  #  .inner_text() возвращает текст, как его видит пользователь
