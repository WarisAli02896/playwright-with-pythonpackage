import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import Page


@pytest.mark.cart
class TestCart:

    def test_added_item_appears_in_cart(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage):
        """TC-11: Item added from inventory is visible in the cart."""
        expected_name = inventory_page.get_item_name_by_index(0)
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart_names = cart_page.get_item_names()
        assert expected_name in cart_names

    def test_remove_item_from_cart(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage):
        """TC-12: Removing an item from the cart empties it."""
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        assert cart_page.get_cart_item_count() == 1
        cart_page.remove_item_by_index(0)
        assert cart_page.is_cart_empty()

    def test_continue_shopping_returns_to_inventory(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage):
        """TC-13: Continue Shopping button navigates back to inventory."""
        inventory_page.go_to_cart()
        cart_page.click_continue_shopping()
        assert "inventory" in cart_page.get_url()

    def test_multiple_items_appear_in_cart(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage):
        """TC-18: Adding 3 items from inventory shows all 3 in the cart."""
        for i in range(3):
            inventory_page.add_item_to_cart_by_index(i)
        inventory_page.go_to_cart()
        assert cart_page.get_cart_item_count() == 3

    def test_cart_price_matches_inventory(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage):
        """TC-24: Item price in cart matches the price shown on inventory."""
        expected_price = inventory_page.get_all_item_prices()[0]
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart_price = float(cart_page.get_item_prices()[0].replace("$", ""))
        assert cart_price == expected_price
