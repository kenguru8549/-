
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time

def test_add_todo(page):  #  значение page это фикстура открытия и закрытия браузера есть в бибилиотеке пайтест
    page.goto("https://zimaev.github.io/navbar/")
    page.locator("li").filter(has_text='Company').click()
    page.locator('li').filter(has=page.locator('.dropdown-toggle')).click()
    page.goto("https://zimaev.github.io/filter/")
    row_locator = page.locator("tr")
    row_locator.filter(has_not=page.get_by_role("button")).count()
    page.goto("https://zimaev.github.io/filter/")
    row_locator = page.locator("tr")
    row_locator.filter(has_not_text="helicopter")
    row_locator = page.locator("tr")
    time.sleep(4)
