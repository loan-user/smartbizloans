import pytest, time
from .reg_common import Loans


@pytest.fixture
def smart_biz(cdriver):
    _smart_biz = Loans(cdriver)
    yield _smart_biz


class TestRegistration:

    def test_registration(self, smart_biz, email_id):

        fname = 'Test User First Name'
        password = 'Test123!'

        smart_biz.loan.launch.launch()
        smart_biz.user_details(fname,
                               'Test User Last Name',
                               email_id,
                               '1234567234',
                               'Test Business',
                               'Radio')
        smart_biz.timeline_data("I’m flexible: about a month works for me")
        smart_biz.duration_data("6 to 12 months ago")
        smart_biz.business_selection('Manufacturing')
        smart_biz.address_selection('378 East St, Bloomsburg, PA')
        smart_biz.entity("Independent Contractor")
        smart_biz.num_employees("6-10 employees")
        smart_biz.business_val("$150,000 - $249,999")

        smart_biz.loan.business.check_pwd_exists()
        assert smart_biz.loan.get_started.duration_pag_is_save_continue_enabled() is False, \
            'Save and Continue button is not disabled'
        smart_biz.url_validation('/apply/prequalify/business/password')

        smart_biz.loan.business.password(password)
        assert smart_biz.loan.get_started.duration_pag_is_save_continue_enabled(), \
            'Save and Continue button is disabled'
        smart_biz.loan.get_started.duration_save_continue()

        smart_biz.loan.get_started.wait_for_sav_cont_to_load()
        smart_biz.url_validation('/apply/prequalify/owners')
        page_heading = smart_biz.loan.business.get_heading()
        assert fname in page_heading, f'{fname} not present in the page heading'

        smart_biz.loan.business.logout_exists()
        smart_biz.loan.business.logout()
        smart_biz.loan.business.yes_signout()

        current_url = smart_biz.loan.customer.get_current_url()
        print(f'Current URL: {current_url}')
        assert '/login' in current_url, \
            '/login not found in the Current URL'

        smart_biz.loan.login.check_login_elem_exists('email')
        smart_biz.loan.login.check_login_elem_exists('password')
        smart_biz.loan.login.check_login_elem_exists('login_to_flow')
        smart_biz.loan.login.email(email_id)
        smart_biz.loan.login.password(password)
        smart_biz.loan.login.login()
        smart_biz.loan.business.wait_for_heading_to_load()
        page_heading = smart_biz.loan.business.get_heading()
        assert fname in page_heading, f'{fname} not present in the page heading, Login UnSuccessful'









