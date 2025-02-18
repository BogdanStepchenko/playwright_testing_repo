import pytest
import allure


@allure.feature('Tests for "Collections Eco Friendly" page')
class TestCollectionsEcoFriendly:

    @pytest.mark.fast_smoke
    @allure.story("Display All Product Cards")
    @allure.severity(allure.severity_level.MINOR)
    def test_displaying_all_product_cards(self, pw_eco_friendly):
        with allure.step("Open the EcoFriendly page"):
            pw_eco_friendly.open_by_url()
        with allure.step("Check that the product counter displays 12 items"):
            pw_eco_friendly.check_that_number_of_displayed_products_in_counter_is(12)
            pw_eco_friendly.check_that_quantity_product_cards_on_screen_is(12)
        with allure.step("Select 24 products per page in the dropdown"):
            pw_eco_friendly.open_selector_and_choose_24()
        with allure.step("Check that the number of displayed product cards is now 18"):
            pw_eco_friendly.check_that_quantity_product_cards_on_screen_is(18)

    @pytest.mark.smoke
    @allure.story("Test Workability of Product List View")
    @allure.severity(allure.severity_level.NORMAL)
    def test_workability_of_products_list_view(self, pw_eco_friendly):
        with allure.step("Open the EcoFriendly page"):
            pw_eco_friendly.open_by_url()
        with allure.step("Switch the product view mode to List View"):
            pw_eco_friendly.change_products_view_to_list()
        with allure.step("Check that the product counter displays 10 items"):
            pw_eco_friendly.check_that_number_of_displayed_products_in_counter_is(10)
            pw_eco_friendly.check_that_quantity_product_cards_on_screen_is(10)

    @pytest.mark.full_test
    @allure.story("Select Products with White Color Only")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_select_products_with_white_color_only(self, pw_eco_friendly):
        with allure.step("Open the EcoFriendly page"):
            pw_eco_friendly.open_by_url()
        with allure.step("Open the filter and select the white color option"):
            pw_eco_friendly.open_color_dropdown_and_select_white_color()
        with allure.step("Verify that all displayed products have the white color tag"):
            pw_eco_friendly.check_that_all_products_has_white_color()
        with allure.step("Check that the product counter matches the number of displayed items"):
            pw_eco_friendly.check_counter_has_correct_value_of_founded_cards()
