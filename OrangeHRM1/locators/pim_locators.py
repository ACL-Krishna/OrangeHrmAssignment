
class PimLocators:

    PIM_MENU = "//span[text()='PIM']"
    ADD_BUTTON = "//button[normalize-space()='Add']"
    FIRST_NAME = "//input[@name='firstName']"
    LAST_NAME = "//input[@name='lastName']"
    SAVE_BUTTON = "//button[@type='submit']"
    SUCCESS_MESSAGE = "//p[contains(@class,'oxd-text--toast-message')]"
    EMPLOYEE_NAME = "(//input[@placeholder= 'Type for hints...'])[1]"
    SEARCH_BUTTON = "//button[normalize-space()='Search']"
    RECORD_FOUND = "//div[@class='oxd-table-body']"
    NO_RECORD = "//span[text()='No Records Found']"