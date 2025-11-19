from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time

def test_add_todo(page):  #  значение page это фикстура открытия и закрытия браузера есть в бибилиотеке пайтест
    page.goto('https://zimaev.github.io/checks-radios/')
    checkbox = page.locator("input")
    for i in range(checkbox.count()):
        checkbox.nth(i).click()


def page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
    checkbox.check()
    pass
