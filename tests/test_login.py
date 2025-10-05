

from pages.login_page import LoginPage
from utils.assertions import assert_url_contains as url_contains
from utils.assertions import assert_error_contains as error_contains
from utils.config import Config
from utils.helpers import take_screenshot

def test_login_pos_01(browser_chrome):
    """
    TC_ID: LOGIN_POS_01
    Title: Login with valid user
    Expected: Redirected to inventory page
    """
    login = LoginPage(browser_chrome)
    login.open()
    login.login(Config.STANDARD_USER, Config.PASSWORD)
    take_screenshot(browser_chrome, step_name="input_pos01")
    # validasi dengan assert import dari module assertion + take screeshot dari utils.helpers
    try:
        url_contains(browser_chrome, "salah")
        take_screenshot(browser_chrome, step_name="result_pos01_as expected")
    except AssertionError as e:
        take_screenshot(browser_chrome, step_name="result_pos01_unexpected")
        raise e

def test_login_neg_01(browser_chrome):
    """
    TC_ID: LOGIN_NEG_01
    Title: Login with locked user
    Expected: Error message displayed
    """
    login = LoginPage(browser_chrome)
    login.open()
    login.login(Config.LOCKED_OUT_USER, Config.PASSWORD)
    take_screenshot(browser_chrome, step_name="input_neg01")
    # validasi
    login.get_error_message()
    actual = login.get_error_message()
    expected = "Epic sadface: Sorry, this user has been locked out."
    try:
        error_contains(actual, expected)
        take_screenshot(browser_chrome, step_name="result_neg01_as expected")
    except AssertionError as e:
        take_screenshot(browser_chrome, step_name="result_neg01_unexpected")
        raise e




#
#     assert "Password is required" in login.get_error_message()

