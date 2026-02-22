from pages.base_page import BasePage
from playwright.sync_api import Page


class CheckoutPage(BasePage):
    SELECTORS = {
        "first_name": "[data-test='firstName']",
        "last_name": "[data-test='lastName']",
        "postal_code": "[data-test='postalCode']",
        "continue_btn": "[data-test='continue']",
        "cancel_btn": "[data-test='cancel']",
        "finish_btn": "[data-test='finish']",
        "back_home_btn": "[data-test='back-to-products']",
        "error_msg": "[data-test='error']",
        "complete_header": ".complete-header",
        "complete_text": ".complete-text",
        "summary_total": ".summary_total_label",
        "title": ".title",
        "cart_items": ".cart_item",
        "item_name": ".inventory_item_name",
    }

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.SELECTORS["first_name"], first_name)
        self.page.fill(self.SELECTORS["last_name"], last_name)
        self.page.fill(self.SELECTORS["postal_code"], postal_code)
        return self

    def click_continue(self):
        self.page.click(self.SELECTORS["continue_btn"])
        return self

    def click_finish(self):
        self.page.click(self.SELECTORS["finish_btn"])
        return self

    def click_cancel(self):
        self.page.click(self.SELECTORS["cancel_btn"])
        return self

    def click_back_home(self):
        self.page.click(self.SELECTORS["back_home_btn"])
        return self

    def get_error_message(self) -> str:
        return self.page.text_content(self.SELECTORS["error_msg"])

    def get_complete_header(self) -> str:
        return self.page.text_content(self.SELECTORS["complete_header"])

    def get_complete_text(self) -> str:
        return self.page.text_content(self.SELECTORS["complete_text"])

    def get_summary_total(self) -> str:
        return self.page.text_content(self.SELECTORS["summary_total"])

    def get_page_title(self) -> str:
        return self.page.text_content(self.SELECTORS["title"])

    def get_checkout_item_names(self) -> list[str]:
        return self.page.locator(self.SELECTORS["item_name"]).all_text_contents()
