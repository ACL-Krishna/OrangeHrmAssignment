class AdminLocators:

    ADMIN_MENU = "text=Admin"
    ADD_BUTTON = "//button[normalize-space()='Add']"
    USER_ROLE = "(//div[contains(@class,'oxd-select-text')])[1]"
    SEARCH_USER_ROLE = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]"
    SEARCH_EMPLOYEE_NAME = "//input[@placeholder='Type for hints...']"
    EMPLOYEE_NAME = "//input[@placeholder='Type for hints...']"
    STATUS = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"
    USERNAME = "//label[text()='Username']/../following-sibling::div//input"
    PASSWORD = "(//input[@type='password'])[1]"
    CONFIRM_PASSWORD = "(//input[@type='password'])[2]"
    SAVE_BUTTON = "//button[@type='submit']"
    SEARCH_USERNAME = "(//input[contains(@class,'oxd-input')])[2]"
    SEARCH_BUTTON = "//button[@type='submit']"
    DELETE_BUTTON = "//div[@role='row'][.//div[text()= AdminData.NEW_USERNAME]]//button[i[contains(@class,'trash')]]"
    CONFIRM_DELETE = "//button[normalize-space()=Yes,Delete']"
    SEARCH_FOUND = "//span[text()='(1) Record Found']"
    RESET_BUTTON = "//button[text()=' Reset ']"






