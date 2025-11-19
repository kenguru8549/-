# project/pages/dashboard_page.py
from playwright.sync_api import Page, expect

class DashboardPage:  #  класс для страницы панели управления, которая появляется после успешного входа
    def __init__(self, page: Page):  #  Конструктор класса DashboardPage принимает объект page и инициализирует локаторы для элементов страницы
        self.page = page  #  сохраняет ссылку на объект страницы для использования в методах класса
        self.profile = page.locator('#usernameDisplay')  #  инициализируют локаторы для элементов страницы
        self.logout = page.locator('#logout')  #  инициализируют локаторы для элемента страницы "Выход"


    def assert_welcome_message(self, message):  #  метод проверяет текст приветственного сообщения на панели управления
        expect(self.profile).to_have_text(message)