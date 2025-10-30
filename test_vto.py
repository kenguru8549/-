from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time


def test_add_todo(page):  #  значение page это фикстура открытия и закрытия браузера есть в бибилиотеке пайтест
    page.goto("https://wifigid.ru/tools/credit-card-generator")
    time.sleep(3)
    page.get_by_label("ФИО").click()
    time.sleep(2)
    page.get_by_placeholder("password")
    time.sleep(3)
    page.locator("//*[@class='fa fa-phone-square fa-fw']").hover()
    time.sleep(3)
    page.locator("//*[@class='fa fa-phone-square fa-fw']").hover()
    time.sleep(3)
