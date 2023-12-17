from math import log as ln, sin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def answer(x):
    return ln(abs(12*sin(int(x))))

def test_book_a_house_for_100_usd(browser):
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    wait = WebDriverWait(browser, 12)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()

    x_value_from_answer = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(answer(x_value_from_answer))
    browser.find_element(By.ID, 'solve').click()

    alert_text = browser.switch_to.alert.text
    finally_answer = alert_text.split(': ')[-1]
    print(finally_answer)