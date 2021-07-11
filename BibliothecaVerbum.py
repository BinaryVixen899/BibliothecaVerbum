import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
opts = ChromeOptions()
opts.headless = True
assert opts.headless == True
browser = Chrome(options=opts)
browser.get('https://duckduckgo.com')
search_form = browser.find_element_by_id('search_form_input_homepage')
print(search_form)
search_form.send_keys('real python')
search_form.submit()
results = browser.find_elements_by_class_name('result')
print(results[0].text)
