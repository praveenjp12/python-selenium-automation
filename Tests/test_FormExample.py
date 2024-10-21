import time

import pytest

from Utils.MainClass import MainClass
from Utils.Assertions import Assertions as Assert

from pages.FormSubmit import FormSubmit as Form

base_url = "https://rahulshettyacademy.com/angularpractice"
expected_text = 'Success! The Form has been submitted successfully!.'

steps = MainClass("Chrome", "full_screen")

@pytest.mark.smoke
def test_form_submit():
    steps.open_url(base_url)
    time.sleep(5)
    steps.type_text(Form.name_input, "Abraham Ozler")
    steps.type_text(Form.email_input, "abrahamoozler@gmail.com")
    steps.type_text(Form.password_input, "Abrah123")
    steps.select_from_dropdown(Form.gender_dropdown_menu, 'Female')
    steps.click_element(Form.ice_cream_checkbox)
    steps.click_element(Form.employment_status_student)
    steps.click_element(Form.submit_button)
    actual_text = steps.get_text(Form.success_message)
    Assert.assert_includes(expected_text, actual_text)
    steps.clear_element(Form.two_way_binding)
    name_after_clearing = steps.get_text(Form.name_input)
    Assert.assert_equals(name_after_clearing, '')
    steps.quit_driver()
