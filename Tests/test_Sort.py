import time

import pytest

from Utils.MainClass import MainClass

from pages.Offers import Offers as Offer

base_url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"

steps = MainClass("Chrome", "full_screen")

def get_element_text():
    p_elements = steps.get_elements(Offer.pagination_buttons)
    vft = []
    for x in range(0, len(p_elements)):
        p_elements[x].click()
        time.sleep(1)
        for ele in steps.get_elements(Offer.veg_fruit_column):
            vft.append(ele.text)
    return vft

@pytest.mark.smoke
def test_sort():
    steps.open_url(base_url)
    before_sorting = get_element_text()
    print(before_sorting)
    before_sorting.sort()
    print(before_sorting)
    steps.click_element(Offer.first_pagination_button)
    steps.click_element(Offer.sort_button)
    after_sorting = get_element_text()
    print(after_sorting)
    assert before_sorting == after_sorting
    steps.quit_driver()

