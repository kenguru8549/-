from playwright.sync_api import Playwright, sync_playwright, expect, Page
import pytest
import time

def test_add_todo(page: Page):
    page.goto("https://test-tkp-sp.secgw.ru/#/index")
    page.get_by_placeholder("Логин").type("Guskov-AV", delay=50)  #  вводит побуквенно
    page.get_by_placeholder("Пароль").press_sequentially("Kotopes1", delay=50) #  ввод посимвольно, дэлэй задержка в милисекундах
    page.get_by_text("Войти").click()
    page.screenshot(path="screenshot2.png")  #  скриншот все страницы, быстрый способ
    pass


def test_add_todo(page: Page):
    page.goto("https://test-tkp-sp.secgw.ru/#/index")
    page.get_by_placeholder("Логин").type("Guskov-AV", delay=50)  #  вводит побуквенно
    page.get_by_placeholder("Пароль").press_sequentially("Kotopes1", delay=50) #  ввод посимвольно, дэлэй задержка в милисекундах
    page.get_by_text("Войти").click()
    page.screenshot(path="screenshot3.png", full_page=True)  #  скриншот все страницы
    pass

def test_add_todo(page: Page):
    page.goto("https://test-tkp-sp.secgw.ru/#/index")
    page.get_by_placeholder("Логин").type("Guskov-AV", delay=50)  #  вводит побуквенно
    page.get_by_placeholder("Пароль").press_sequentially("Kotopes1", delay=50) #  ввод посимвольно, дэлэй задержка в милисекундах
    page.get_by_text("Войти").click()
    page.locator(".user-fullname").screenshot(path="screenshot.png")  #  скриншот веб-элемента
    pass


