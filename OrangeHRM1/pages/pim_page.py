
from locators.pim_locators import PimLocators

class PimPage:
    def __init__(self,page):
        self.page=page

    def open_pim(self):
        self.page.click(PimLocators.PIM_MENU)

    def add_employee(self,first_name,last_name):
        self.open_pim()
        self.page.click(PimLocators.ADD_BUTTON)
        self.page.fill(PimLocators.FIRST_NAME,first_name)
        self.page.fill(PimLocators.LAST_NAME,last_name)
        self.page.click(PimLocators.SAVE_BUTTON)
        self.page.wait_for_selector(PimLocators.SUCCESS_MESSAGE)

    def search_employee(self,employee):
        self.open_pim()
        self.page.fill(PimLocators.EMPLOYEE_NAME,employee)
        self.page.click(PimLocators.SEARCH_BUTTON)
        self.page.wait_for_timeout(3000)




