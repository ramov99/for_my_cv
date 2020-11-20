from pages.catalogue_page import CataloguePage
from random import randint


def test_user_can_add_random_available_item_to_basket(browser):
    # Arrange
    catalogue_page = CataloguePage(browser)
    catalogue_page.open()

    # Act - should parametrize page number here and not hard-code it
    catalogue_page.go_to_next_page(3)
    available_items, _ = catalogue_page.get_items_availability()
    random_available_item = available_items[randint(1, len(available_items))]
    item_title = catalogue_page.get_item_title_as_text(random_available_item)
    item_price = catalogue_page.get_item_price_as_text(random_available_item)
    catalogue_page.add_item_to_cart(random_available_item)

    # Assert
    catalogue_page.verify_item_added_to_cart(item_title, item_price)

