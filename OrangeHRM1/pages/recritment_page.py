
from locators.recruitment_locators import RecruitmentLocators

class RecruitmentPage:

    def __init__(self,page):
        self.page=page

    def add_candidate(self,first,last,email):
        self.page.click(RecruitmentLocators.RECRUITMENT)
        self.page.click(RecruitmentLocators.ADD_BUTTON)
        self.page.fill(RecruitmentLocators.FIRST_NAME,first)
        self.page.fill(RecruitmentLocators.LAST_NAME, last)
        self.page.fill(RecruitmentLocators.EMAIL, email)
        self.page.click(RecruitmentLocators.SAVE_BUTTON)
