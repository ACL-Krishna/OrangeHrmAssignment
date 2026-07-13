

from locators.admin_locators import AdminLocators
from testdata.admin_data import AdminData
class AdminPage:
    def __init__(self,page):
        self.page=page

    def open_admin(self):
        self.page.locator(AdminLocators.ADMIN_MENU).wait_for(state="visible")
        self.page.locator(AdminLocators.ADMIN_MENU).click()

    def create_user(self,username,password):
        self.open_admin()
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.ADD_BUTTON).click()
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.USER_ROLE).click()
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(3000)
        employee = self.page.locator(AdminLocators.EMPLOYEE_NAME)
        employee.fill(AdminData.EMPLOYEE_NAME)
        self.page.wait_for_timeout(3000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.STATUS).click()
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.locator(AdminLocators.USERNAME).wait_for(state="visible")
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.USERNAME).fill(username)
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.PASSWORD).fill(password)
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.CONFIRM_PASSWORD).fill(password)
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.SAVE_BUTTON).click()
        self.page.wait_for_timeout(4000)

    def search_user(self,username):
        self.open_admin()
        self.page.wait_for_timeout(1000)
        search = self.page.locator(AdminLocators.SEARCH_USERNAME)
        search.wait_for(state="visible")
        search.fill(username)
        user_role = self.page.locator(AdminLocators.SEARCH_USER_ROLE)
        user_role.wait_for(state="visible")
        user_role.click()
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        search_employee = self.page.locator(AdminLocators.SEARCH_EMPLOYEE_NAME)
        search_employee.wait_for(state="visible")
        self.page.wait_for_timeout(3000)
        search_employee.fill(AdminData.EMPLOYEE_NAME_SEARCH)
        self.page.wait_for_timeout(3000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.STATUS).click()
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1000)
        self.page.locator(AdminLocators.SEARCH_BUTTON).click()
        self.page.wait_for_timeout(1000)


