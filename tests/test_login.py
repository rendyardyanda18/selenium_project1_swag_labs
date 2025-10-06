from conftest import run_timestamp
from pages.login_page import LoginPage
from utils.assertions import Assertions as asserts
from utils.config import Config
from utils.helpers import take_screenshot
from locators.login_locators import LoginLocators

def test_login_pos_01(browser_chrome,run_timestamp):
    """
    TC_ID: LOGIN_POS_01
    Title: Login with valid credentials
    Expected: Redirected to inventory page
    """
    login = LoginPage(browser_chrome)
    login.open()
    login.login_input(Config.STANDARD_USER, Config.PASSWORD)
    take_screenshot(browser_chrome, step_name="input_pos01",run_timestamp=run_timestamp)
    login.login_button()
    # validasi dengan assert import dari module assertion + take screeshot dari utils.helpers
    try:
        asserts.assert_url_contains(browser_chrome, "inventory")
        take_screenshot(browser_chrome, step_name="result_pos01_as expected",run_timestamp=run_timestamp)
    except AssertionError as e:
        take_screenshot(browser_chrome, step_name="result_pos01_unexpected",run_timestamp=run_timestamp)
        raise e

def test_login_neg_01(browser_chrome,run_timestamp):
    """
    TC_ID: LOGIN_NEG_01
    Title: Login with locked user
    Expected:
        - Error message appears
        - Showed message "This user has been locked"
    """
    login = LoginPage(browser_chrome)
    login.open()
    login.login_input(Config.LOCKED_OUT_USER, Config.PASSWORD)
    login.login_button()
    take_screenshot(browser_chrome, step_name="input_neg01", run_timestamp=run_timestamp)
    # validasi element tampil
    asserts.assert_element_displayed(
        lambda: login.error_message(),
        step_name="Error locked user"
    )
    # validasi message error
    login.get_error_message()
    actual = login.get_error_message()
    expected = "This user has been locked out."
    try:
        asserts.assert_error_contains(actual, expected)
        take_screenshot(browser_chrome, step_name="result_neg01_as expected",run_timestamp=run_timestamp)
    except AssertionError as e:
        take_screenshot(browser_chrome, step_name="result_neg01_unexpected",run_timestamp=run_timestamp)
        raise e

def test_login_neg_06(browser_chrome,run_timestamp):
    """
    TC_ID: LOGIN_NEG_06
    Title: Login with username input only
    Expected:
        - Error message appears
        - Showed message "Please enter your password."
    """
    l = LoginPage(browser_chrome)
    l.open()
    l.login_input(Config.STANDARD_USER,Config.PASSWORD)
    take_screenshot(browser_chrome, step_name="input_neg06", run_timestamp=run_timestamp)
    l.login_button()
    # validasi element tampil
    asserts.assert_element_displayed(
        lambda: l.error_message(),
        step_name="Error password null"
    )
    # validasi message error
    actual = l.get_error_message()
    expected = "Please enter your password."
    try:
        asserts.assert_error_contains(actual, expected)
        take_screenshot(browser_chrome, step_name="result_neg06_as expected",run_timestamp=run_timestamp)
    except AssertionError as e:
        take_screenshot(browser_chrome, step_name="result_neg06_unexpected",run_timestamp=run_timestamp)
        raise e

def test_login_neg_07(browser_chrome,run_timestamp):
    """
    TC_ID: LOGIN_NEG_07
    Title: Login with password input only
    Expected:
        - Error message appears
        - Showed message "Please enter your username."
    """
    l = LoginPage(browser_chrome)
    l.open()
    l.login_input(" ",Config.PASSWORD)
    take_screenshot(browser_chrome, step_name="input_neg07", run_timestamp=run_timestamp)
    l.login_button()
    # validasi element tampil
    asserts.assert_element_displayed(
        lambda: l.error_message(),
        step_name="Error username null"
    )
    # validasi message error
    actual = l.get_error_message()
    expected = "Please enter your username."
    try:
        asserts.assert_error_contains(actual, expected)
        take_screenshot(browser_chrome, step_name="result_neg07_as expected",run_timestamp=run_timestamp)
    except AssertionError as e:
        take_screenshot(browser_chrome, step_name="result_neg07 _unexpected",run_timestamp=run_timestamp)
        raise e

def test_login_neg_08(browser_chrome,run_timestamp):
    """
    TC_ID: LOGIN_NEG_08
    Title: Login with password input only
    Expected:
        - Error message appears
        - Showed message "Please input username and password"
    """
    l = LoginPage(browser_chrome)
    l.open()
    l.login_input(" ",Config.PASSWORD)
    take_screenshot(browser_chrome, step_name="input_neg08", run_timestamp=run_timestamp)
    l.login_button()
    # validasi element tampil
    asserts.assert_element_displayed(
        lambda: l.error_message(),
        step_name="Error username null"
    )
    # validasi message error
    actual = l.get_error_message()
    expected = "Please input username and password"
    try:
        asserts.assert_error_contains(actual, expected)
        take_screenshot(browser_chrome, step_name="result_neg08_as expected",run_timestamp=run_timestamp)
    except AssertionError as e:
        take_screenshot(browser_chrome, step_name="result_neg08 _unexpected",run_timestamp=run_timestamp)
        raise e
