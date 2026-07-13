
class RecruitmentLocators:

    RECRUITMENT = "//span[text()='Recruitment']"
    ADD_BUTTON  = "//button[normalize-space()='Add']"
    FIRST_NAME = "//input[@name='firstName']"
    LAST_NAME = "//input[@name='lastName']"
    EMAIL = "(//input[@placeholder='Type here'])[2]"
    SAVE_BUTTON = "//button[@type='submit']"
    SUCCESS = "//p[contains(@class,'oxd-text--toast--message')]"