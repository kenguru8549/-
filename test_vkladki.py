from playwright.sync_api import Playwright, sync_playwright, expect, Page
import pytest
import time


def test_new_tab(page):
    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value  #  позволяет выполнять действия над новой страницей
    time.sleep(3)
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"  #  проверим, что url данной вкладки соответсвует нужному с помощью assert
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')  #  Найдем элемент в панели навигации c текстом Sign out
    assert sign_out.is_visible()  #  проверим его на видимость




