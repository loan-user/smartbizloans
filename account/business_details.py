from smartbizloans import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select as WebDriverSelect
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Business(Page):

    locators = {

        'business_industry': 'label[for="business_type_id"]>select',
        'heading': 'h1[class="page-subheader-zilla"]',
        'address': 'input[id="street"]',
        'apt': 'input[id^="apt_"]',

        'addr_list': 'div[id="PlacesAutocomplete__root"]>div[role="listbox"]',
        'entity': 'select[id="entity_type_id"]',
        'password': 'password',
        'logout': 'logout-link'

    }

    def wait_for_business_to_load(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                    self.locators['business_industry'])))

    def select_business(self, value):
        WebDriverSelect(self.driver.find_element_by_css_selector(self.locators['business_industry'])).\
            select_by_visible_text(value)

    def wait_for_address_to_load(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                    self.locators['address'])))

    def address(self, addr):
        mail = self.driver.find_element_by_css_selector(self.locators['address'])
        mail.send_keys(addr)

    def click_apartment(self):
        mail = self.driver.find_element_by_css_selector(self.locators['apt'])
        mail.click()

    def business_located(self):
        business = self.driver.find_element_by_css_selector(self.locators['heading'])
        business.click()

    def wait_for_heading_to_load(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                    self.locators['heading'])))

    def get_heading(self):
        heading = self.driver.find_element_by_css_selector(self.locators['heading'])
        return heading.text

    def wait_for_popped_addr(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                    self.locators['addr_list'])))

    def addr_from_list(self):
        addr = self.driver.find_element_by_css_selector(self.locators['addr_list'])
        addr.click()

    def wait_for_business_entity_to_load(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                    self.locators['entity'])))

    def select_business_entity(self, value):
        WebDriverSelect(self.driver.find_element_by_css_selector(self.locators['entity'])).select_by_visible_text(value)

    def wait_for_pwd_to_load(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.ID,
                                                    self.locators['password'])))

    def check_pwd_exists(self):
        try:
            self.driver.\
                find_element_by_id(self.locators['password'])
        except NoSuchElementException:
            raise NoSuchElementException('Password field not found')

    def password(self, password):
        pwd = self.driver.find_element_by_id(self.locators['password'])
        pwd.send_keys(password)

    def logout_exists(self):
        try:
            self.driver.\
                find_element_by_id(self.locators['logout'])
        except NoSuchElementException:
            raise NoSuchElementException('Password field not found')

    def logout(self):
        self.driver.find_element_by_id(self.locators['logout']).click()

    def yes_signout(self):
        self.driver.find_element_by_xpath('//div[@class="sb-alert"]/div/a[text()="Yes, sign me out"]').click()
