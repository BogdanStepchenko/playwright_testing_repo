import pytest
import allure
from pages.helper.text_to_check import SUCCESS_REG_TEXT
from pages.helper.text_to_check import REQUIRED_FIELD_TEXT, PSWRD_CONFIRMATION_ERROR_TEXT


@allure.feature('Tests for "Sign In Page" page')
class TestSignInPage:
    @pytest.mark.fast_smoke
    @allure.story("Impossible to Create Account Without Data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_impossible_to_create_account_without_data(self, pw_sign_in_page):
        with allure.step("Open the Sign In Page and get the current URL"):
            url = pw_sign_in_page.open_by_url()
        with allure.step("Click on the 'Create Account' button without filling any fields"):
            pw_sign_in_page.click_on_create_account_button()
        with allure.step("Check if error messages for all required fields appear"):
            pw_sign_in_page.check_error_appeared_for_all_fields(REQUIRED_FIELD_TEXT)
        with allure.step("Check if the URL has not changed"):
            pw_sign_in_page.check_url_was_not_changed(url)

    @pytest.mark.smoke
    @allure.story("Account Creation with Incorrect Password Confirmation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_account_creation_with_incorrect_password_confirmation(self, pw_sign_in_page):
        with allure.step("Open the Sign In Page"):
            pw_sign_in_page.open_by_url()
        with allure.step("Fill in the first name"):
            pw_sign_in_page.fill_first_name()
        with allure.step("Fill in the last name"):
            pw_sign_in_page.fill_last_name()
        with allure.step("Fill in the email address"):
            pw_sign_in_page.fill_email()
        with allure.step("Fill in the password"):
            pw_sign_in_page.fill_password()
        with allure.step("Fill in the incorrect password confirmation"):
            pw_sign_in_page.fill_incorrect_password_confirmation()
        with allure.step("Click on the 'Create Account' button"):
            pw_sign_in_page.click_on_create_account_button()
        with allure.step("Check if the password confirmation error message appears"):
            pw_sign_in_page.check_if_password_confirmation_error_appeared(PSWRD_CONFIRMATION_ERROR_TEXT)

    @pytest.mark.full_test
    @allure.story("Correct Account Creation")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_correct_account_creation(self, pw_sign_in_page, pw_account_page):
        with allure.step("Open the Sign In Page and get the current URL"):
            url = pw_sign_in_page.open_by_url()
        with allure.step("Fill in all fields with correct data"):
            pw_sign_in_page.fill_all_fields_with_correct_data()
        with allure.step("Click on the 'Create Account' button"):
            pw_sign_in_page.click_on_create_account_button()
        with allure.step("Check if the URL has changed to the account page"):
            pw_account_page.check_url_was_changed(url)
        with allure.step("Check if the success message appears after account creation"):
            pw_account_page.check_success_message_appeared(SUCCESS_REG_TEXT)
