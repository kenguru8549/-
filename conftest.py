import pytest
@pytest.fixture(scope="function") #  устанавливает размер браузера
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.mark.skip_browser("firefox")  #  пропустить какой-то тест или в данном случае браузер фаерфркс
def test_visit_example(page):
    page.goto("https://example.com")
    # ...
    pass


@pytest.mark.only_browser("chromium")  # запустить какой-то тест или в данном случае браузер хром
def test_visit_example(page):
    page.goto("https://example.com")
    # ...
    pass