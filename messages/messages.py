class LoginMessages:
    LOGIN_SUCCESS = "Login successful"
    LOCKED_OUT_ERROR = "Epic sadface: Sorry, this user has been locked out."
    INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
    USERNAME_REQUIRED = "Epic sadface: Username is required"
    PASSWORD_REQUIRED = "Epic sadface: Password is required"


class CartMessages:
    ITEM_ADDED = "Item added to cart"
    ITEM_REMOVED = "Item removed from cart"
    CART_EMPTY = "Cart is empty"


class CheckoutMessages:
    FIRST_NAME_REQUIRED = "Error: First Name is required"
    LAST_NAME_REQUIRED = "Error: Last Name is required"
    POSTAL_CODE_REQUIRED = "Error: Postal Code is required"
    ORDER_COMPLETE_HEADER = "Thank you for your order!"
    ORDER_COMPLETE_TEXT = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
