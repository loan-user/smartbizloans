import pytest
from selenium import webdriver
from random import randint


@pytest.fixture()
def cdriver():
    driver = webdriver.Chrome(r'C:\Drivers\chromedriver.exe')
    driver.maximize_window()
    yield driver


@pytest.fixture()
def email_id():
    return f'test.automation{randint(1000,9999)}@smartbizloans.com'