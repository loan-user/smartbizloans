from smartbizloans import Loan


class Loans(Loan):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

        self.loan = Loan(self.driver)

    def url_validation(self, url_value):
        current_url = self.loan.customer.get_current_url()
        print(f'Current URL: {current_url}')
        assert url_value in current_url, f'{url_value} not found in the Current URL'

    def user_details(self, fname: str, lname: str, email_id:str, phone:str, business:str, hear_abt: str):
        self.loan.customer.check_form_elements_exists()
        self.loan.customer.check_how_to_use_loan()
        assert self.loan.customer.is_submit_enabled() is False, 'Continue to pre-qualify is enabled'
        self.loan.customer.check_sba_loan()
        self.loan.customer.first_name(fname)
        self.loan.customer.last_name(lname)
        self.loan.customer.email(email_id)
        self.loan.customer.phone(phone)
        self.loan.customer.business(business)
        self.loan.customer.select_hear_abt_us(hear_abt)
        self.loan.customer.acceptance()
        assert self.loan.customer.is_submit_enabled(), 'Continue to pre-qualify is disabled'
        self.loan.customer.accept_cookie_window()
        self.loan.customer.submit()

    def timeline_data(self, timeline):
        self.loan.get_started.wait_for_get_started_to_load()
        self.url_validation('/apply/loan')
        self.loan.get_started.get_started()
        self.loan.get_started.wait_for_elem_to_load("I have a strict timeline: 2 weeks or less")
        self.url_validation('apply/prequalify/financing_needs')

        self.loan.get_started.check_button_exists("I have a strict timeline: 2 weeks or less")
        self.loan.get_started.check_button_exists("I’m flexible: about a month works for me")
        self.loan.get_started.check_button_exists("I don’t have a specific time in mind")
        assert self.loan.get_started.is_save_continue_enabled() is False, \
            'Save and Continue button is not disabled'
        self.loan.get_started.click_button(timeline)
        assert self.loan.get_started.is_save_continue_enabled(), 'Save and Continue button is not enabled'
        self.loan.get_started.save_continue()

    def duration_data(self, duration):
        self.loan.get_started.wait_for_elem_to_load("Less than 6 months ago")
        # smart_biz.loan.get_started.wait_for_page_to_load()
        self.url_validation('/apply/prequalify/business/inception_date')

        self.loan.get_started.check_button_exists("Less than 6 months ago")
        self.loan.get_started.check_button_exists("6 to 12 months ago")
        self.loan.get_started.check_button_exists("13 to 24 months ago")
        self.loan.get_started.check_button_exists("25 to 60 months ago")
        self.loan.get_started.check_button_exists("61 to 120 months ago")
        self.loan.get_started.check_button_exists("More than 120 months ago")
        assert self.loan.get_started.duration_pag_is_save_continue_enabled() is False, \
            'Save and Continue button is not disabled'

        self.loan.get_started.click_button(duration)
        assert self.loan.get_started.duration_pag_is_save_continue_enabled(), \
            'Save and Continue button is not enabled'

        self.loan.get_started.duration_save_continue()

    def business_selection(self, business):
        self.loan.business.wait_for_business_to_load()
        self.url_validation('/apply/prequalify/business/industry')

        assert self.loan.get_started.duration_pag_is_save_continue_enabled() is False, \
            'Save and Continue button is not disabled'

        self.loan.business.select_business(business)
        assert self.loan.get_started.duration_pag_is_save_continue_enabled(), \
            'Save and Continue button is not enabled'
        self.loan.get_started.duration_save_continue()

    def address_selection(self, addr):
        self.loan.business.wait_for_address_to_load()
        self.url_validation('/apply/prequalify/business/address')
        assert self.loan.get_started.duration_pag_is_save_continue_enabled() is False, \
            'Save and Continue button is not disabled'

        self.loan.business.address(addr)
        # time.sleep(5)
        self.loan.business.wait_for_popped_addr()
        self.loan.business.addr_from_list()
        self.loan.business.click_apartment()
        self.loan.business.business_located()
        self.loan.get_started.duration_save_continue()

    def entity(self, name):
        self.loan.business.wait_for_business_entity_to_load()
        assert self.loan.get_started.duration_pag_is_save_continue_enabled() is False, \
            'Save and Continue button is not disabled'
        self.loan.business.select_business_entity("Independent Contractor")
        self.loan.get_started.duration_save_continue()

    def num_employees(self, count):
        self.loan.get_started.wait_for_elem_to_load("No employees – just me")
        self.url_validation('/apply/prequalify/business/employees')

        self.loan.get_started.check_button_exists("No employees – just me")
        self.loan.get_started.check_button_exists("1-5 employees")
        self.loan.get_started.check_button_exists("6-10 employees")
        self.loan.get_started.check_button_exists("11-20 employees")
        self.loan.get_started.check_button_exists("More than 20 employees")

        self.loan.get_started.click_button(count)

        assert self.loan.get_started.duration_pag_is_save_continue_enabled(), \
            'Save and Continue button is not enabled'
        self.loan.get_started.duration_save_continue()

    def business_val(self, value):
        self.loan.get_started.wait_for_elem_to_load("$150,000 - $249,999")
        self.loan.get_started.click_button(value)
        self.loan.get_started.duration_save_continue()

        self.loan.business.wait_for_pwd_to_load()