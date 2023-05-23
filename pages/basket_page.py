from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def is_not_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Should not be products in basket if there is an empty basket message"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FREE_ELEMENT), \
            "Should be message about empty basket if there are not any products in basket"
