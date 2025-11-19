from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time


def test_add_todo(page):  #  значение page это фикстура открытия и закрытия браузера есть в бибилиотеке пайтест
    page.goto("https://wifigid.ru/tools/credit-card-generator")
    time.sleep(3)
    page.get_by_label("ФИО").check()  #  заполнение чекбокса, радиобатона или свитча
    time.sleep(1)
    page.get_by_label("CVV").uncheck()  #  снятие флага с чекбокса, радиобатона или свитча
    page.get_by_label("По порядку").check()
    page.select_option('.form-control', label="MasterCard")  #  выбор значения из выпадашки по имени
    page.select_option('.form-control', index=0)  #  выбор значения из выпадашки по индексу
    time.sleep(2)
    #  page.select_option('#skills', value=["playwright", "python"]) если мультиселектор пишем массив
    # Переходим к иконке телефона и выполняем действие hover
    phone_icon = page.locator("//*[@class='fa fa-phone-square fa-fw']")
    expect(phone_icon).to_be_visible(timeout=5000)
    phone_icon.hover()
    time.sleep(3)
