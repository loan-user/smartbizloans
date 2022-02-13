from smartbizloans.launch import Launch
from smartbizloans.account import Login, Customer, GetStarted, Business


class Loan:

    def __init__(self, driver):
        self.driver = driver
        self.launch = Launch(self.driver)
        self.login = Login(self.driver)
        self.customer = Customer(self.driver)
        self.get_started = GetStarted(self.driver)
        self.business = Business(self.driver)