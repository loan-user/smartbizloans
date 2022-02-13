from smartbizloans import Page
from selenium.webdriver.support.select import Select as WebDriverSelect
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Customer(Page):

    locators = {

        'how_to_use_loan': 'form[id="preferences-selection"] '
                           'label[id="square-selector-label-0"] div[class="box relative"]>i',
        'sba_loan': '//label[@id="square-simple-selector-label-1"]/div/div/i',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email_id': 'email',
        'phone_number': 'phone',
        'business_name': 'legal_business_name',
        'hear_abt_us': 'referral_source',
        'accept_policy': 'input[id="privacy_policy"]',
        'submit': 'a[id="submit_apply_form"]',
        'cookie': 'div[id="cookieConsentModal"]>div[class="pf-bar-content"]>span>button',
    }

    def check_how_to_use_loan(self):
        self.driver.find_element_by_css_selector(self.locators['how_to_use_loan']).click()

    def check_sba_loan(self):
        self.driver.execute_script("window.scrollTo(0,1000);")
        sba_loan = self.driver.find_element_by_xpath(self.locators['sba_loan'])
        ActionChains(self.driver).move_to_element(sba_loan).click(sba_loan).perform()

    def first_name(self, fname):
        name = self.driver.find_element_by_id(self.locators['first_name'])
        name.send_keys(fname)

    def last_name(self, lname):
        name = self.driver.find_element_by_id(self.locators['last_name'])
        name.send_keys(lname)

    def email(self, eid):
        mail = self.driver.find_element_by_id(self.locators['email_id'])
        mail.send_keys(eid)

    def phone(self, number):
        ph_number = self.driver.find_element_by_id(self.locators['phone_number'])
        ph_number.send_keys(number)

    def business(self, name):
        business_name = self.driver.find_element_by_id(self.locators['business_name'])
        business_name.send_keys(name)

    def select_hear_abt_us(self, value):
        WebDriverSelect(self.driver.find_element_by_id(self.locators['hear_abt_us'])).select_by_visible_text(value)

    def acceptance(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.find_element_by_css_selector(self.locators['accept_policy']).click()

    def submit(self):
        self.driver.find_element_by_css_selector(self.locators['submit']).click()

    def is_submit_enabled(self):
        submit = self.driver.find_element_by_css_selector(self.locators['submit'])
        class_attrib = submit.get_attribute("class")
        print(f' Submit button Class attribute: {class_attrib}')
        return False if 'disabled' in class_attrib else True

    def accept_cookie_window(self):
        self.driver.find_element_by_css_selector(self.locators['cookie']).click()

    def check_form_elements_exists(self):
        all_locators = [self.locators['first_name'],
                        self.locators['last_name'],
                        self.locators['email_id'],
                        self.locators['phone_number'],
                        self.locators['business_name'],
                        self.locators['hear_abt_us']
                        ]
        try:
            for item in all_locators:
                self.driver.find_element_by_id(item)
        except NoSuchElementException:
            raise NoSuchElementException("One of the form element is missing")

    def get_current_url(self):
        return self.driver.current_url

