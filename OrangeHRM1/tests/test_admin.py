import pytest
from playwright.sync_api import expect
from locators.admin_locators import AdminLocators
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from testdata.login_data import LoginData
from testdata.admin_data import AdminData

class TestAdmin:

    def test_create_user(self,page):
        LoginPage(page).login(LoginData.VALID_USERNAME,LoginData.VALID_PASSWORD)
        admin=AdminPage(page)
        admin.create_user(AdminData.NEW_USERNAME,AdminData.NEW_PASSWORD)
        page.wait_for_timeout(3000)
        added_user1 = page.locator(f"//div[text()='{AdminData.NEW_USERNAME}']")
        assert added_user1.is_visible()



