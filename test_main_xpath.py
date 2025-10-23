
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time




def test_add_todo(page):  #  значение page это фикстура открытия и закрытия браузера есть в бибилиотеке пайтест
    page.goto("https://www.wikipedia.org/")
    page.locator("//*[@id='js-link-box-ru']").click()
    page.locator("//*[@id='simpleSearch']").click()
    page.locator("//*[@class='vector-search-box-input']").fill("Сборная России по футболу")
    time.sleep(1)
    page.locator("//*[@class='vector-search-box-input']").press('Enter')
    time.sleep(1)
    page.locator("//*[@href='/wiki/%D0%A7%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%B0%D1%82_%D0%BC%D0%B8%D1%80%D0%B0_%D0%BF%D0%BE_%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D1%83_2018']").nth(8).hover() # наведение курсора на элемент, nht - задает номер элемента если их несколько
    time.sleep(3)
    page.locator("//*[@placeholder='Искать в Википедии']").click()
    time.sleep(6)
    page.get_by_text("Артём Сергеевич").click()  # ищет вхождение части текста в текст общий, встроен в плейрайт
    time.sleep(6)
    page.get_by_text("Артём Сергеевич", exact=True).nth(0).click()  # ищет вхождение части текста в текст общий
    time.sleep(2)
