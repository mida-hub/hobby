import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.yahoo.co.jp')

# time.sleep(5)
# driver.find_element_by_link_text("ニュース").click()

# time.sleep(5)
# driver.back()

time.sleep(5)
driver.find_element_by_css_selector("._1wsoZ5fswvzAoNYvIJgrU4").send_keys("Python")
time.sleep(1)
driver.find_element_by_css_selector(".PHOgFibMkQJ6zcDBLbga8").click()
