from pages.login_page import LoginPage
from testdata.login_data import LoginData
from locators.login_locators import LoginLocators

class TestLogin:

    def test_valid_login(self,page):
        login = LoginPage(page)
        login.login(username=LoginData.VALID_USERNAME,
                    password=LoginData.VALID_PASSWORD)
        page.wait_for_timeout(3000)
        assert page.title() == "OrangeHRM"

    def test_invalid_password(self, page):
        login = LoginPage(page)
        login.login(username=LoginData.VALID_USERNAME,
                    password=LoginData.INVALID_PASSWORD)
        invalid_text=page.locator(LoginLocators.INVALID_CREDENTIAL).inner_text()
        assert invalid_text == LoginData.INVALID_CREDENTIALS

    def test_invalid_username(self, page):
        login = LoginPage(page)
        login.login(username=LoginData.INVALID_USERNAME,
                    password=LoginData.VALID_PASSWORD)
        invalid_text = page.locator(LoginLocators.INVALID_CREDENTIAL).inner_text()
        assert invalid_text == LoginData.INVALID_CREDENTIALS

    def test_blank_credentials(self, page):
        login = LoginPage(page)
        login.click_login()
        assert page.locator(LoginLocators.BLANK_CREDENTIALS).count() == 2

