from playwright.sync_api import Playwright, sync_playwright, expect, Page
import pytest
import time

def poluch(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_text())
    pass
def poluch2(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_text_contents())  #  не работают методы
    pass
def test_add_todo(page: Page):
    page.goto("https://test-tkp-sp.secgw.ru/#/index")
    page.get_by_placeholder("Логин").type("Guskov-AV", delay=50)  #  вводит побуквенно
    page.get_by_placeholder("Пароль").press_sequentially("Kotopes1", delay=50) #  ввод посимвольно, дэлэй задержка в милисекундах
    page.get_by_text("Войти").click()
    page.get_by_text("Льготники").click()
    time.sleep(4)
    row = page.locator("tr")
    print(row.all_inner_texts())  #  отработало


def test_add_todo(page: Page):
    page.goto("https://test-tkp-sp.secgw.ru/#/index")
    page.get_by_placeholder("Логин").type("Guskov-AV", delay=50)  #  вводит побуквенно
    page.get_by_placeholder("Пароль").press_sequentially("Kotopes1", delay=50) #  ввод посимвольно, дэлэй задержка в милисекундах
    page.get_by_text("Войти").click()
    page.get_by_text("Льготники").click()
    time.sleep(4)
    row = page.locator("tr")
    print(row.all_text_contents())  #  отработало