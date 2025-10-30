
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time




def test_add_todo(page):  #  значение page это фикстура открытия и закрытия браузера есть в бибилиотеке пайтест
    page.goto("https://www.wikipedia.org/")
    page.locator('#js-link-box-ru').click()
    page.locator('#simpleSearch').click()
    page.locator('.vector-search-box-input').fill("Сборная России по футболу")
    page.locator('.vector-search-box-input').press('Enter')
    page.locator("[href='/wiki/%D0%A1%D0%B1%D0%BE%D1%80%D0%BD%D0%B0%D1%8F_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_%D0%BF%D0%BE_%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D1%83']").click()
    page.locator("[href='/wiki/%D0%A7%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%B0%D1%82_%D0%BC%D0%B8%D1%80%D0%B0_%D0%BF%D0%BE_%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D1%83_2018']").nth(8).hover()  # наведение курсора на элемент, nht - задает номер элемента если их несколько
    page.locator("[placeholder='Искать в Википедии']").click()
    page.get_by_text("Артём Сергеевич").click() #ищет вхождение части текста в текст общий
    page.get_by_text("Клубная", exact=True).nth(0).click()  # ищет точное совпадение с экзект тру
    page.get_by_placeholder("Искать в Википедии").click()  # ищет по плейсхолдеру в поле
    page.get_by_alt_text("Флаг России").nth(5).click()  # для картинок
    time.sleep(2)
    page.get_by_title("Закрыть этот инструмент (Esc)").click()  # указания дополнительной информации об элементе
    time.sleep(2)
    selector = page.get_by_title("Перейти к странице, имеющей в точности такое название").and_(page.locator("//*[@id='searchButton']"))
    selector.click()
    time.sleep(2)