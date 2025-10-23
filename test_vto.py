from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time


def test_add_todo(page):  #  значение page это фикстура открытия и закрытия браузера есть в бибилиотеке пайтест
    page.goto("https://test-tkp-lko.secgw.ru/#/login")
    time.sleep(3)
    page.get_by_label("Логин").fill('Kvaga')
    time.sleep(3)