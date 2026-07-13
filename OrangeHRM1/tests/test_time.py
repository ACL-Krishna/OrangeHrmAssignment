
from pages.login_page import LoginPage
from pages.time_page import TimePage

class TestTime:

    def test_create_timesheet(self,logged_in_page):
        time = TimePage(logged_in_page)
        time.create_timesheet()