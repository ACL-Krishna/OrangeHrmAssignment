import pytest
from pages.login_page import LoginPage
from pages.recritment_page import RecruitmentPage
from testdata.recruit_data import RecruitData

class TestRecruitment:

    @pytest.mark.parametrize("candidate",RecruitData.CANDIDATES)
    def test_add_candidate(self,logged_in_page,candidate):
        recruit = RecruitmentPage(logged_in_page)
        recruit.add_candidate(candidate["first"],candidate["last"],
                              candidate["email"])















    # def test_add_candidate2(self,page):
    #     LoginPage(page).login("Admin","admin123")
    #     recruit = RecruitmentPage(page)
    #     recruit.add_candidate(
    #         "Priyanka",
    #         "Sharma",
    #         "priyanka@test.com")

