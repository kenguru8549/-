from playwright.sync_api import Playwright, sync_playwright, expect, Page
import pytest
import time

def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()
    pass

def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept())  #  подтверждает в попапе действие (ОК), попап с да и нет
    page.get_by_text("Диалог Confirmation").click()
    time.sleep(3)
    pass

def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.dismiss())  #  отвергает в попапе действие (Отмена), попап с да и нет
    page.get_by_text("Диалог Confirmation").click()
    time.sleep(3)
    pass

def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept())  #  подтверждает в попапе действие (ОК), попап с ОК
    page.get_by_text("Диалог Alert").click()
    time.sleep(3)
    pass

def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.dismiss())  #  отвергает в попапе действие (Отмена), с вводом данных
    page.get_by_text("Диалог Prompt").click()
    time.sleep(3)
    pass

def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.once("dialog", lambda dlg: dlg.accept("555"))  #  отвергает в попапе действие (Отмена), с вводом данных
    page.locator('#prompt-button').click()
    time.sleep(3)




