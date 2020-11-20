from .product_page import ProductPage
from .base_page import BasePage


class OfferPage(ProductPage):

    def __init__(self, browser, offer_link):
        product_page_offer_link = f"{OfferPage.PRODUCT_PAGE_LINK}{offer_link}"
        BasePage.__init__(self, browser, product_page_offer_link)
