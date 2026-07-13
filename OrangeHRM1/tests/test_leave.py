
from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from testdata.leave_data import LeaveData
from locators.leave_locators import LeaveLocators

class TestLeave:

    def test_search_leave(self,logged_in_page):
        leave = LeavePage(logged_in_page)
        leave.search_leave(LeaveData.DATE_FROM,LeaveData.DATE_TO)
        record_found = logged_in_page.locator(LeaveLocators.RECORD_FOUND).inner_text()
        assert LeaveData.search_record in record_found

    def test_apply_leave(self,logged_in_page):
        leave = LeavePage(logged_in_page)
        #leave.apply_leave(LeaveData.DATE_FROM,LeaveData.DATE_TO)
        leave.apply_leave(LeaveData.DATE_FROM,LeaveData.DATE_TO)
        apply_leave_text = logged_in_page.locator(LeaveLocators.APPLY_LEAVE_TEXT).inner_text()
        assert apply_leave_text == LeaveData.apply_leave_found





