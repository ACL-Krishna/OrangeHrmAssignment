
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from testdata.pim_data import PimData
from locators.pim_locators import PimLocators

class TestPIM:

    def test_add_employee(self, logged_in_page):
        PimPage(logged_in_page).add_employee(PimData.EMPLOYEE_1["first_name"],PimData.EMPLOYEE_1["last_name"])
        assert logged_in_page.locator(PimLocators.SUCCESS_MESSAGE).is_visible()

    def test_add_employee2(self, logged_in_page):
        PimPage(logged_in_page).add_employee(PimData.EMPLOYEE_2["first_name"],PimData.EMPLOYEE_2["last_name"])
        assert logged_in_page.locator(PimLocators.SUCCESS_MESSAGE).is_visible()

    def test_invalid_employee(self, logged_in_page):
        PimPage(logged_in_page).search_employee(PimData.INVALID_EMPLOYEE)
        logged_in_page.wait_for_selector(PimLocators.NO_RECORD)
        assert logged_in_page.locator(PimLocators.NO_RECORD).is_visible()
