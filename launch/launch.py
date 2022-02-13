from smartbizloans import Page


class Launch(Page):

    url = "https://qa-www.smartbizloans.com/apply?partner_id=smartbiz"

    def launch(self):
        self.driver.get(self.url)
