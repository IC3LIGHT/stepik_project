from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.CARD_BUTTON)
        link.click()

    def should_be_button(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#add_to_basket_form > button"), "Button isn't available"

    def success_message(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not presented"
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_BASKET), "Message about adding is not presented"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name in message, 'No book name in the message'

    def price_test(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Price is not presented"
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_BASKET), "Price in basket is not presented"
        message_basket_total = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        product_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert product_price in message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDING), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDING), \
            "Success message is not disappeared"
