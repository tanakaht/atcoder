import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import chromedriver_binary
import time

clipboard = pyperclip.paste()

output_path = sys.argv[1]
with open(output_path) as f:
    output_ = f.read()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://img.atcoder.jp/future-contest-2022-qual/f4ca7c3336de23e5c8d1338981e38375.html")
ele = driver.find_element_by_xpath('/html/body/div/span/span/section/div[2]/div[2]/div[1]/textarea')
pyperclip.copy(output_)
actions = ActionChains(driver)
actions.move_to_element(ele)
actions.click(ele) #select the element where to paste text
actions.key_down(Keys.META)
actions.send_keys('v')
actions.key_up(Keys.META)
actions.perform()
pyperclip.copy(clipboard)
# driver.execute_script(f"document.getElementById('output').value='{output_}'")
driver.find_element_by_xpath('/html/body/div/span/span/section/div[2]/div[3]/input').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/span/span/section/div[2]/div[4]/form/table/tbody/tr/th[1]/div/button').click()
time.sleep(1000)
