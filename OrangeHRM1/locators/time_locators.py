
class TimeLocators:

    TIME = "//span[text()='Time']"
    #TIMESHEET = "//a[text()='Timesheets']"
    TIMESHEET = "(//i[@class='oxd-icon bi-chevron-down'])[1]"
    MY_TIMESHEET = "//a[text()='My Timesheets']"
    EDIT = "//button[normalize-space()='Edit']"
    SAVE = "//button[@type='submit']"