from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    SELECTORS = {
        "username": "#user-name",
        "password": "#password",
        "login_btn": "#login-button",
        "error_msg": "[data-test='error']",
        "error_close_btn": ".error-button",
    }

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate(self.URL)
        return self

    def enter_username(self, username: str):
        self.page.fill(self.SELECTORS["username"], username)
        return self

    def enter_password(self, password: str):
        self.page.fill(self.SELECTORS["password"], password)
        return self

    def click_login(self):
        self.page.click(self.SELECTORS["login_btn"])
        return self

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self) -> str:
        return self.page.text_content(self.SELECTORS["error_msg"])

    def is_error_displayed(self) -> bool:
        return self.page.is_visible(self.SELECTORS["error_msg"])
