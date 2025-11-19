from playwright.sync_api import Playwright, sync_playwright, expect, Page, expect
import pytest
import time


def test_inventory(page):  #  GET запрос на эндпоинт, используйте метод page.request.get() с указанием url.
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.status)  #  узнать код ответа от сервера на запрос
    print(response.json())  #  узнать код ответа от сервера с помощью методов .json(), .body(), .text()
    pass


def test_add_user(page):  #  POST запрос на эндпоинт, используйте метод page.request.post()  c указанием url, тела и заголовков
    data = [  ##  тело запроса
              {
                "id": 9743,
                "username": "fsfd",
                "firstName": "ffff",
                "lastName": "gggg",
                "email": "bbbb",
                "password": "ttt",
                "phone": "3333",
                "userStatus": 0
              }
            ]
    header = {  #  заголовки запроса
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray', data=data, headers=header)
    print(response.status)  #  узнать код ответа от сервера на запрос
    print(response.json())