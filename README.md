# Playwright Web Automation Framework (Python)

Automated test suite for [SauceDemo](https://www.saucedemo.com) built with **Playwright + Pytest** using the **Page Object Model** pattern.

## Project Structure

```
Playwright-web-Automation/
├── config/             # Environment configuration
├── messages/           # Expected messages & constants
├── pages/              # Page Object Model classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/              # Test cases
│   ├── test_login.py       (TC-01 to TC-05)
│   ├── test_inventory.py   (TC-06 to TC-10)
│   ├── test_cart.py        (TC-11 to TC-13)
│   └── test_checkout.py    (TC-14 to TC-15)
├── utils/              # Helper utilities
├── reports/            # HTML reports & screenshots
├── conftest.py         # Pytest fixtures
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Python dependencies
└── .env                # Environment variables
```

## Setup

```bash
pip install -r requirements.txt
playwright install chromium
```

## Running Tests

```bash
# Run all tests
pytest

# Run by marker
pytest -m smoke
pytest -m login
pytest -m cart
pytest -m checkout

# Run headed (visible browser)
pytest --headed

# Run specific test file
pytest tests/test_login.py
```

## Test Cases

| ID    | Test                                   | Module     |
|-------|----------------------------------------|------------|
| TC-01 | Valid login                            | Login      |
| TC-02 | Locked-out user error                  | Login      |
| TC-03 | Empty username error                   | Login      |
| TC-04 | Empty password error                   | Login      |
| TC-05 | Invalid credentials error              | Login      |
| TC-06 | Products displayed after login         | Inventory  |
| TC-07 | Sort by price low to high              | Inventory  |
| TC-08 | Sort by name Z to A                    | Inventory  |
| TC-09 | Add product shows cart badge           | Inventory  |
| TC-10 | Remove product updates badge           | Inventory  |
| TC-11 | Added item appears in cart             | Cart       |
| TC-12 | Remove item from cart                  | Cart       |
| TC-13 | Continue shopping returns to inventory | Cart       |
| TC-14 | Checkout with empty fields error       | Checkout   |
| TC-15 | Complete checkout flow end-to-end      | Checkout   |
