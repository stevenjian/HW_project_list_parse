from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome()

browser.get('http://eip/rd2/Lists/HW%20Project%20List/AllItems.aspx')
elem=browser.find_element(By.XPATH, '//*[@id="bottomPagingCellWPQ2"]/table/tbody/tr/td[2]/a/img')
actions = ActionChains(browser)
actions.click(elem).perform()
