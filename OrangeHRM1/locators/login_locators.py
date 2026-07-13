
class LoginLocators:

    USERNAME = "//input[@name='username']"
    PASSWORD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    ERROR_MESSAGE = "//p[contains(@class, 'oxd-alert-content-text')]"
    REQUIRED = "//span[text()='Required']"
    DASHBOARD = "//h6[text()='Dashboard']"
    PROFILE   = "//span[@class,oxd-userdropdown-tab']"
    LOGOUT ="//a[text()='Logout']"
    INVALID_CREDENTIAL = "//p[text()='Invalid credentials']"
    BLANK_CREDENTIALS = "//span[text()='Required']"