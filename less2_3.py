from selenium import webdriver 
import time
import math
link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(12)
    browser.find_element_by_xpath("//*[text()='$100']")
    browser.find_element_by_id("book").click()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("#solve").click()



finally:
    time.sleep(10)
    browser.quit()
