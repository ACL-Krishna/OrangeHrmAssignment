
class LeaveLocators:

    LEAVE_MENU = "//span[text()='Leave']"
    APPLY_MENU = "//a[text()='Apply']"
    LEAVE_TYPE = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"
    #LEAVE_TYPE = "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    FORM_DATE = "(//input[@class='oxd-input oxd-input--active'])[2]"
    #FORM_DATE = "//lable[text()='From Date']/../following-sibling::div//input"
    TO_DATE  = "(//input[@class='oxd-input oxd-input--active'])[2]"
    #TO_DATE = "xpath=//label[text()='To Date']/ancestor::div[contains(@class,'oxd-input-group)]//input"
    APPLY_BUTTON = "//button[@type='submit']"
    MY_LEAVE  = "//a[text()='My Leave']"
    SEARCH_BUTTON = "//button[text()=' Search ']"
    RECORD_TABLE = "//div[@class='oxd-table-body']"
    RECORD_FOUND = "//span[text()='No Records Found']"
    APPLY_LEAVE_TEXT = "//p[text()='No Leave Types with Leave Balance']"