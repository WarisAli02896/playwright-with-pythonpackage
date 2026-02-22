import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from messages.messages import CheckoutMessages
from utils.helpers import generate_random_string, generate_random_zip
from playwright.sync_api import Page


@pytest.mark.checkout
class TestCheckout:

    def test_checkout_with_empty_fields(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage, checkout_page: CheckoutPage):
        """TC-14: Submitting checkout with empty fields shows validation error."""
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.click_continue()
        assert checkout_page.get_error_message() == CheckoutMessages.FIRST_NAME_REQUIRED

    def test_complete_checkout_flow(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage, checkout_page: CheckoutPage):
        """TC-15: Full end-to-end checkout completes successfully."""
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart_page.click_checkout()

        checkout_page.fill_checkout_info(
            generate_random_string(),
            generate_random_string(),
            generate_random_zip(),
        )
        checkout_page.click_continue()

        assert checkout_page.get_page_title() == "Checkout: Overview"
        checkout_page.click_finish()

        assert checkout_page.get_complete_header() == CheckoutMessages.ORDER_COMPLETE_HEADER
        assert checkout_page.get_complete_text() == CheckoutMessages.ORDER_COMPLETE_TEXT

    def test_checkout_missing_last_name(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage, checkout_page: CheckoutPage):
        """TC-19: Submitting checkout without last name shows specific error."""
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.fill_checkout_info(generate_random_string(), "", "")
        checkout_page.click_continue()
        assert checkout_page.get_error_message() == CheckoutMessages.LAST_NAME_REQUIRED

    def test_back_home_after_checkout(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage, checkout_page: CheckoutPage):
        """TC-20: Back Home button after order returns to inventory."""
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.fill_checkout_info(
            generate_random_string(),
            generate_random_string(),
            generate_random_zip(),
        )
        checkout_page.click_continue()
        checkout_page.click_finish()
        checkout_page.click_back_home()
        assert "inventory" in checkout_page.get_url()

    def test_checkout_missing_postal_code(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage, checkout_page: CheckoutPage):
        """TC-22: Submitting checkout without postal code shows specific error."""
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.fill_checkout_info(generate_random_string(), generate_random_string(), "")
        checkout_page.click_continue()
        assert checkout_page.get_error_message() == CheckoutMessages.POSTAL_CODE_REQUIRED

    def test_checkout_overview_shows_correct_item(self, logged_in_page: Page, inventory_page: InventoryPage, cart_page: CartPage, checkout_page: CheckoutPage):
        """TC-25: Checkout overview displays the same item that was added to cart."""
        expected_name = inventory_page.get_item_name_by_index(0)
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart_page.click_checkout()
        checkout_page.fill_checkout_info(
            generate_random_string(),
            generate_random_string(),
            generate_random_zip(),
        )
        checkout_page.click_continue()
        assert expected_name in checkout_page.get_checkout_item_names()
