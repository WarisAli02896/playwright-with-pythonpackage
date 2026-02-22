from pages.base_page import BasePage
from playwright.sync_api import Page


class CartPage(BasePage):
    SELECTORS = {
        "title": ".title",
        "cart_items": ".cart_item",
        "item_name": ".inventory_item_name",
        "item_price": ".inventory_item_price",
        "remove_btn": "[data-test^='remove']",
        "checkout_btn": "[data-test='checkout']",
        "continue_shopping_btn": "[data-test='continue-shopping']",
        "cart_quantity": ".cart_quantity",
    }

    def __init__(self, page: Page):
        super().__init__(page)

    def get_page_title(self) -> str:
        return self.page.text_content(self.SELECTORS["title"])

    def get_cart_item_count(self) -> int:
        return self.page.locator(self.SELECTORS["cart_items"]).count()

    def get_item_names(self) -> list[str]:
        return self.page.locator(self.SELECTORS["item_name"]).all_text_contents()

    def get_item_prices(self) -> list[str]:
        return self.page.locator(self.SELECTORS["item_price"]).all_text_contents()

    def remove_item_by_index(self, index: int = 0):
        self.page.locator(self.SELECTORS["remove_btn"]).nth(index).click()
        return self

    def click_checkout(self):
        self.page.click(self.SELECTORS["checkout_btn"])
        return self

    def click_continue_shopping(self):
        self.page.click(self.SELECTORS["continue_shopping_btn"])
        return self

    def is_cart_empty(self) -> bool:
        return self.get_cart_item_count() == 0
