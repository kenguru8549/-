from playwright.sync_api import Playwright, sync_playwright, expect, Page
import pytest
import time

def test_add_todo(page: Page):
    page.goto("https://test-tkp-sp.secgw.ru/#/index")
    page.get_by_placeholder("Логин").type("Guskov-AV", delay=50)  #  вводит побуквенно
    page.get_by_placeholder("Пароль").press_sequentially("Kotopes1", delay=50) #  ввод посимвольно, дэлэй задержка в милисекундах
    page.get_by_text("Войти").click()
    page.get_by_text("Льготники").click()
    time.sleep(4)
    page.locator("//*[@class='el-table__row']").nth(1).dblclick()
    page.once("dialog", lambda dialog: dialog.accept())  #  подтверждает в попапе действие, при once делает это единажды, подписка на один раз(Отмена)
    page.get_by_text("Изменить").click()
    page.get_by_text("Транспортная карта").click()
    page.get_by_placeholder("Номер карты").fill('99900000211')
    time.sleep(5)
    page.get_by_text("Добавить").nth(1).click()
    time.sleep(5)


