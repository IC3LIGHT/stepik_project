from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    CARD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    BOOK_PRICE_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME = (By.CLASS_NAME, "content h1")
    ADDING = (By.CSS_SELECTOR, 'div.alertinner ')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_FREE_ELEMENT = (By.CSS_SELECTOR, "#content_inner>p")
