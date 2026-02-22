import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import Config
from messages.messages import LoginMessages


@pytest.mark.smoke
@pytest.mark.login
class TestLogin:

    def test_valid_login(self, login_page: LoginPage, inventory_page: InventoryPage):
        """TC-01: Valid login navigates to inventory page."""
        login_page.open().login(Config.STANDARD_USER, Config.PASSWORD)
        assert "inventory" in login_page.get_url()
        assert inventory_page.get_page_title() == "Products"

    def test_locked_out_user(self, login_page: LoginPage):
        """TC-02: Locked-out user sees an error message."""
        login_page.open().login(Config.LOCKED_USER, Config.PASSWORD)
        assert login_page.is_error_displayed()
        assert login_page.get_error_message() == LoginMessages.LOCKED_OUT_ERROR

    def test_empty_username(self, login_page: LoginPage):
        """TC-03: Empty username shows required error."""
        login_page.open().enter_password(Config.PASSWORD).click_login()
        assert login_page.get_error_message() == LoginMessages.USERNAME_REQUIRED

    def test_empty_password(self, login_page: LoginPage):
        """TC-04: Empty password shows required error."""
        login_page.open().enter_username(Config.STANDARD_USER).click_login()
        assert login_page.get_error_message() == LoginMessages.PASSWORD_REQUIRED

    def test_invalid_credentials(self, login_page: LoginPage):
        """TC-05: Invalid credentials show mismatch error."""
        login_page.open().login("wrong_user", "wrong_pass")
        assert login_page.is_error_displayed()
        assert login_page.get_error_message() == LoginMessages.INVALID_CREDENTIALS
