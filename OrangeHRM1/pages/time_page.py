
from locators.time_locators import TimeLocators

class TimePage:

    def __init__(self,page):
        self.page = page

    def create_timesheet(self):
        #self.page.click(TimeLocators.TIME)
        self.page.locator(TimeLocators.TIME).wait_for(state="visible")
        self.page.locator(TimeLocators.TIME).click()
        self.page.wait_for_timeout(2000)
        self.page.locator(TimeLocators.TIMESHEET).wait_for(state="visible")
        self.page.click(TimeLocators.TIMESHEET)
        self.page.wait_for_timeout(2000)
        self.page.click(TimeLocators.MY_TIMESHEET)
        self.page.click(TimeLocators.EDIT)
        self.page.click(TimeLocators.SAVE)
