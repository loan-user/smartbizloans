from smartbizloans import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select as WebDriverSelect
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Login(Page):

    locators = {
        'email': 'email',
        'password': 'password',
        'login': 'login_to_flow',
    }

    def check_login_elem_exists(self, id):
        try:
            self.driver.\
                find_element_by_id(id)
        except NoSuchElementException:
            raise NoSuchElementException(f'Login page: {id} does not exist')

    def email(self, email):
        elem = self.driver.find_element_by_id(self.locators['email'])
        elem.send_keys(email)

    def password(self, pwd):
        elem = self.driver.find_element_by_id(self.locators['password'])
        elem.send_keys(pwd)

    def login(self):
        self.driver.find_element_by_id(self.locators['login']).click()
