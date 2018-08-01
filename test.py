from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://liginc.co.jp/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element_by_link_text('ブログトップ').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 10秒待機する
sleep(6)

# ブラウザの終了
driver.close()
