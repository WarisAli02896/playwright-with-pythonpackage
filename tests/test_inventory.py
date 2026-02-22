import pytest
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page


@pytest.mark.smoke
@pytest.mark.inventory
class TestInventory:

    def test_products_displayed(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-06: Products are listed on the inventory page after login."""
        assert inventory_page.get_inventory_count() == 6
        assert inventory_page.get_page_title() == "Products"

    def test_sort_by_price_low_to_high(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-07: Sorting by price low-to-high orders items correctly."""
        inventory_page.sort_by("lohi")
        prices = inventory_page.get_all_item_prices()
        assert prices == sorted(prices)

    def test_sort_by_name_z_to_a(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-08: Sorting by name Z-A reverses alphabetical order."""
        inventory_page.sort_by("za")
        names = inventory_page.get_all_item_names()
        assert names == sorted(names, reverse=True)

    def test_add_product_shows_cart_badge(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-09: Adding a product increments the cart badge."""
        inventory_page.add_item_to_cart_by_index(0)
        assert inventory_page.get_cart_badge_count() == 1
        inventory_page.add_item_to_cart_by_index(1)
        assert inventory_page.get_cart_badge_count() == 2

    def test_remove_product_updates_badge(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-10: Removing a product decrements the cart badge."""
        inventory_page.add_item_to_cart_by_index(0)
        assert inventory_page.get_cart_badge_count() == 1
        inventory_page.remove_item_by_index(0)
        assert inventory_page.get_cart_badge_count() == 0

    def test_sort_by_price_high_to_low(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-16: Sorting by price high-to-low orders items descending."""
        inventory_page.sort_by("hilo")
        prices = inventory_page.get_all_item_prices()
        assert prices == sorted(prices, reverse=True)

    def test_logout_redirects_to_login(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-17: Logout from inventory returns to the login page."""
        inventory_page.logout()
        assert inventory_page.get_url() == "https://www.saucedemo.com/"

    def test_sort_by_name_a_to_z(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-21: Default sort order is alphabetical A-Z."""
        inventory_page.sort_by("az")
        names = inventory_page.get_all_item_names()
        assert names == sorted(names)

    def test_each_product_has_description(self, logged_in_page: Page, inventory_page: InventoryPage):
        """TC-23: Every product on the inventory page has a non-empty description."""
        count = inventory_page.get_inventory_count()
        for i in range(count):
            desc = inventory_page.get_item_description_by_index(i)
            assert desc and len(desc.strip()) > 0
