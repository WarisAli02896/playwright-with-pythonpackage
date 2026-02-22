from pages.base_page import BasePage
from playwright.sync_api import Page


class InventoryPage(BasePage):
    SELECTORS = {
        "title": ".title",
        "inventory_list": ".inventory_list",
        "inventory_items": ".inventory_item",
        "item_name": ".inventory_item_name",
        "item_price": ".inventory_item_price",
        "add_to_cart_btn": "[data-test^='add-to-cart']",
        "remove_btn": "[data-test^='remove']",
        "cart_badge": ".shopping_cart_badge",
        "cart_link": ".shopping_cart_link",
        "sort_dropdown": "[data-test='product-sort-container']",
        "burger_menu": "#react-burger-menu-btn",
        "logout_link": "#logout_sidebar_link",
        "item_description": ".inventory_item_desc",
    }

    def __init__(self, page: Page):
        super().__init__(page)

    def get_page_title(self) -> str:
        return self.page.text_content(self.SELECTORS["title"])

    def get_all_item_names(self) -> list[str]:
        return self.page.locator(self.SELECTORS["item_name"]).all_text_contents()

    def get_all_item_prices(self) -> list[float]:
        prices = self.page.locator(self.SELECTORS["item_price"]).all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def get_inventory_count(self) -> int:
        return self.page.locator(self.SELECTORS["inventory_items"]).count()

    def add_item_to_cart_by_index(self, index: int = 0):
        self.page.locator(self.SELECTORS["add_to_cart_btn"]).nth(index).click()
        return self

    def remove_item_by_index(self, index: int = 0):
        self.page.locator(self.SELECTORS["remove_btn"]).nth(index).click()
        return self

    def get_cart_badge_count(self) -> int:
        if self.page.is_visible(self.SELECTORS["cart_badge"]):
            return int(self.page.text_content(self.SELECTORS["cart_badge"]))
        return 0

    def go_to_cart(self):
        self.page.click(self.SELECTORS["cart_link"])
        return self

    def sort_by(self, value: str):
        """Values: az, za, lohi, hilo"""
        self.page.select_option(self.SELECTORS["sort_dropdown"], value)
        return self

    def logout(self):
        self.page.click(self.SELECTORS["burger_menu"])
        self.page.click(self.SELECTORS["logout_link"])
        return self

    def get_item_name_by_index(self, index: int = 0) -> str:
        return self.page.locator(self.SELECTORS["item_name"]).nth(index).text_content()

    def get_item_description_by_index(self, index: int = 0) -> str:
        return self.page.locator(self.SELECTORS["item_description"]).nth(index).text_content()
