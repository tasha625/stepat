from selenium import webdriver
import math
from selenium import webdriver
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # browser.execute_script("alert('Robots at work');")
    # browser.execute_script("document.title='Script executing';")
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")

    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()
    input3 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()
    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
