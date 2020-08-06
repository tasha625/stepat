import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_find(browser, link):
    browser.get(link)
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".quiz-component .textarea")))
    text_area = browser.find_element_by_css_selector(".quiz-component .textarea")
    answer = math.log(int(time.time()))
    text_area.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    text = browser.find_element_by_css_selector(".smart-hints__hint").text
    print(text)

