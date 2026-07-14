
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from testdata.login_data import LoginData

class TestDashboard:

    def test_dashboard(self,page):
        LoginPage(page).login(LoginData.VALID_USERNAME,LoginData.VALID_PASSWORD)
        dashboard = DashboardPage(page)
        dashboard.verify_dashboard()

    def test_dashboard_widgets(self,page):
        LoginPage(page).login(LoginData.VALID_USERNAME,LoginData.VALID_PASSWORD)
        dashboard = DashboardPage(page)
        dashboard.verify_dashboard()
        dashboard.verify_widgets()
