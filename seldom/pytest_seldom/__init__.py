import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def chrome():
    browser = webdriver.Chrome()
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def firefox():
    browser = webdriver.Firefox()
    yield browser
    browser.close()