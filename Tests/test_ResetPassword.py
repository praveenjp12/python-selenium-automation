import random
import string

import pytest

from Utils.MainClass import MainClass
from Utils.Assertions import Assertions as Assert

from pages.SignIn import SignIn as Signin

base_url = "https://rahulshettyacademy.com/client"
homepage_url = 'https://rahulshettyacademy.com/client/dashboard/dash'
homepage_title = "Let's Shop"
user_email = ((''.join(random.choice(string.ascii_uppercase + string.digits)
                       for i in range(20))).lower()
              + '@testing.com')
user_pass = 'Pass#1234556789'
wrong_pass = 'Qwerty!2345'
new_pass = 'HAIhello!234'

steps = MainClass("Chrome", "mobile_screen")

steps.wait_seconds(10)

@pytest.mark.smoke
def test_create_account():
    steps.open_url(base_url)
    steps.scroll_to_element(Signin.create_account_link)
    steps.click_element(Signin.create_account_link)
    steps.scroll_to_element(Signin.firstname_field)
    steps.type_text(Signin.firstname_field, 'Abraham')
    steps.type_text(Signin.lastname_filed, 'Ozler')
    steps.type_text(Signin.user_email_input, user_email)
    steps.type_text(Signin.phone_number_input, '9876543210')
    steps.type_text(Signin.user_password_input, user_pass)
    steps.type_text(Signin.confirm_password_input, user_pass)
    steps.scroll_to_element(Signin.user_consent)
    steps.click_element(Signin.user_consent)
    steps.scroll_to_element(Signin.register_button)
    steps.click_element(Signin.register_button)

@pytest.mark.smoke
def test_reset_password():
    steps.open_url(base_url)
    steps.type_text(Signin.email_input, user_email)
    steps.type_text(Signin.password_input, wrong_pass)
    steps.scroll_to_element(Signin.login_button)
    steps.click_element(Signin.login_button)
    steps.is_visible(Signin.toast_error_message)
    error_message = steps.get_text(Signin.toast_error_message)
    Assert.assert_equals('Incorrect email or password.', error_message)
    steps.scroll_to_element(Signin.forgot_password_link)
    steps.click_element(Signin.forgot_password_link)
    steps.type_text(Signin.user_email_input, user_email)
    steps.type_text(Signin.user_password_input, new_pass)
    steps.type_text(Signin.confirm_password_input, new_pass)
    steps.scroll_to_element(Signin.save_password_button)
    steps.click_element(Signin.save_password_button)

@pytest.mark.smoke
def test_sign_in():
    steps.open_url(base_url)
    steps.type_text(Signin.email_input, user_email)
    steps.type_text(Signin.password_input, new_pass)
    steps.scroll_to_element(Signin.login_button)
    steps.click_element(Signin.login_button)
    steps.wait_until_element_is_present(Signin.brand_logo)
    current_url = steps.get_url()
    Assert.assert_equals(homepage_url, current_url)
    current_title = steps.get_title()
    Assert.assert_equals(homepage_title, current_title)
    steps.quit_driver()
