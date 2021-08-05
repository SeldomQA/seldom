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


@pytest.fixture(scope="session")
def safari():
    browser = webdriver.Safari()
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def edge():
    browser = webdriver.Edge()
    yield browser
    browser.close()
