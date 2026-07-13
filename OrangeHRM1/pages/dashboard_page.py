
from locators.dashboard_locators import DashboardLocators

class DashboardPage:
    def __init__(self,page):
        self.page=page

    def verify_dashboard(self):
        self.page.wait_for_selector(DashboardLocators.DASHBOARD)
        assert self.page.locator(DashboardLocators.DASHBOARD).is_visible()


    def verify_widgets(self):
        self.page.wait_for_selector(DashboardLocators.TIME_AT_WORK)
        assert self.page.locator(DashboardLocators.TIME_AT_WORK).is_visible()
        assert self.page.locator(DashboardLocators.MY_ACTION).is_visible()
        assert self.page.locator(DashboardLocators.QUICK_LAUNCH).is_visible()