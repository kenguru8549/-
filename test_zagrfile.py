from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time
def test_select_multiple2(page):
    page.goto("https://test-tkp-sp.secgw.ru/#/index")
    page.get_by_placeholder("Логин").type("Guskov-AV", delay=50)  # вводит побуквенно
    page.get_by_placeholder("Пароль").press_sequentially("Kotopes1", delay=50)  # ввод посимвольно, дэлэй задержка в милисекундах
    page.get_by_text("Войти").click()
    page.get_by_text("Льготники").click()
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("Импорт льготника.csv"))
    page.get_by_text("Обработать").click()
    page.get_by_placeholder("Регион").click()
    page.get_by_text("ZK-КАВКАЗ").click()
    page.get_by_placeholder("Действие").click()
    page.get_by_text("Заблокировать льготы").click()
    time.sleep(3)



