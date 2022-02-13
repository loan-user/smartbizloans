from smartbizloans import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select as WebDriverSelect
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class GetStarted(Page):

    locators = {

        'lets_get_started': 'a[id="apply_loading"]>div[class="flex-box center"]',
        'save_continue': 'a[id="financial_needs_new_prequal"]',
        'save_continue_owner': 'owners_new_prequal',
        'years_save_continue': 'a[id="password_new_prequal"]',
    }

    def wait_for_get_started_to_load(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators['lets_get_started'])))

    def get_started(self):
        self.driver.find_element_by_css_selector(self.locators['lets_get_started']).click()

    def wait_for_elem_to_load(self, button_text):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.XPATH,
                                                    f'//div[@class="info-content"]/span[text()="{button_text}"]')))

    def check_button_exists(self, button_text):
        try:
            self.driver.\
                find_element_by_xpath(f'//div[@class="info-content"]/span[text()="{button_text}"]')
        except NoSuchElementException:
            raise NoSuchElementException(f"Button : {button_text} not found")

    def wait_for_sav_cont_to_load(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.ID,
                                                    self.locators['save_continue_owner'])))

    def is_save_continue_enabled(self):
        submit = self.driver.find_element_by_css_selector(self.locators['save_continue'])
        class_attrib = submit.get_attribute("class")
        print(f'Save Continue: Class attribute: {class_attrib}')
        return False if 'disabled' in class_attrib else True

    def save_continue(self):
        self.driver.find_element_by_css_selector(self.locators['save_continue']).click()

    def duration_pag_is_save_continue_enabled(self):
        submit = self.driver.find_element_by_css_selector(self.locators['years_save_continue'])
        class_attrib = submit.get_attribute("class")
        print(f'Save Continue: Class attribute: {class_attrib}')
        return False if 'disabled' in class_attrib else True

    def duration_save_continue(self):
        self.driver.find_element_by_css_selector(self.locators['years_save_continue']).click()

    def click_button(self, button_text):
        self.driver.find_element_by_xpath(f'//div[@class="info-content"]/span[text()="{button_text}"]').click()

    def wait_for_years_load(self):
        WebDriverWait(self.driver, 100). \
            until(EC.visibility_of_element_located((By.XPATH, self.locators['strict_timeline'])))

    def home_page_displayed(self):
        WebDriverWait(self.driver, 200).until(EC.visibility_of_element_located((By.XPATH, self.locators['home_page'])))
