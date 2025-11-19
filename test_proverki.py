from playwright.sync_api import Playwright, sync_playwright, expect, Page, expect
import pytest
import time

def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")  #  проверяем, что открытая страница имеет нужный адрес
    input_field = page.get_by_placeholder('What needs to be done?')  #  сохраняем в переменную локатор пустого поля
    expect(input_field).to_be_empty()  #  проверяем, что поле пустое
    input_field.fill("Закончить курс по playwright")  #  заполняем поле первым значением
    input_field.press('Enter')
    input_field.fill("Добавить в резюме, что умею автоматизировать")  #  заполняем поле вторым значением
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')  #  проверяем количество введенных значений, записываем в переменную
    expect(todo_item).to_have_count(2) #  проверяем, что количество введенных значений = 2
    todo_item.get_by_role('checkbox').nth(0).click()  #  нажимаем на чекбокс
    expect(todo_item.nth(0)).to_have_class('completed')  #  проверяем, что чекбокс с флагом(активен)
    expect(todo_item.nth(1)).to_have_class('completed')
