
import pytest
from playwright.sync_api import sync_playwright
from config.config import Config
from pages.login_page import LoginPage
from testdata.pim_data import PimData
from utilities.logger import Logger

@pytest.fixture(scope="function")
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=Config.HEADLESS)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.BASE_URL)

    yield page
    context.close()
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def logged_in_page(page):
    LoginPage(page).login(PimData.USERNAME,PimData.PASSWORD)
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome= yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            Logger.info(f"{item.name} PASSED")
        elif report.failed:
            Logger.error(f"{item.name} FAILED")












