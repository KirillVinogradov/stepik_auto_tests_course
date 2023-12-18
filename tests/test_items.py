from selenium.webdriver.common.by import By

URL = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_page_contains_add_to_basket_button(browser):
    browser.get(URL)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert add_to_basket_button is not None, 'The button was not found'