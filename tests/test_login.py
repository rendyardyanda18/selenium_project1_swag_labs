

from pages.login_page import LoginPage
from utils.assertions import assert_url_contains as url_contains
from utils.helpers import take_screenshot

def test_login_pos_01(browser_chrome):
    """
    TC_ID: LOGIN_POS_01
    Title: Login with valid user
    Expected: Redirected to inventory page
    """
    login = LoginPage(browser_chrome)
    login.open()
    take_screenshot(browser_chrome, step_name="before_login")
    login.login("standard_user", "secret_sauce")

    # validasi dengan assert import dari module assertion
    # url_contains(browser_chrome, "inventory")
    # validasi dengan assert import dari module assertion + take screeshot dari utils.helpers
    try:
        url_contains(browser_chrome, "inventory")
        take_screenshot(browser_chrome, step_name="login_success")
    except AssertionError as e:
        take_screenshot(browser_chrome, step_name="login_failed")
        raise e


#
#
# @pytest.mark.negative
# def test_login_neg_01(driver):
#     """
#     TC_ID: LOGIN_NEG_01
#     Title: Login with empty password
#     Expected: Error message displayed
#     """
#     login = LoginPage(driver)
#     login.open()
#     login.login("standard_user", "")
#
#     assert "Password is required" in login.get_error_message()

