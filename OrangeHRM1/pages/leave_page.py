
from locators.leave_locators import LeaveLocators

class LeavePage:
    def __init__(self,page):
        self.page=page


    def open_leave(self):
        self.page.click(LeaveLocators.LEAVE_MENU)

    def search_leave(self,from_date,to_date):
        self.open_leave()
        self.page.wait_for_timeout(3000)
        self.page.click(LeaveLocators.MY_LEAVE)
        self.page.wait_for_timeout(3000)
        self.page.fill(LeaveLocators.FORM_DATE,from_date)
        self.page.wait_for_timeout(3000)
        self.page.fill(LeaveLocators.FORM_DATE,from_date)
        self.page.wait_for_timeout(3000)
        self.page.locator(LeaveLocators.LEAVE_TYPE).click()
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(3000)
        self.page.click(LeaveLocators.SEARCH_BUTTON)
        self.page.wait_for_timeout(3000)

    def apply_leave(self,from_date,to_date):
        self.open_leave()
        self.page.click(LeaveLocators.APPLY_MENU)
        self.page.wait_for_timeout(2000)
     








