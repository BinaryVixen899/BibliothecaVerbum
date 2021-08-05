import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
opts = ChromeOptions()
opts.headless = True
assert opts.headless == True
browser = Chrome(options=opts)
browser.get('https://www.goodreads.com/quotes/tag/harry-potter?page=1')
results = browser.find_elements_by_class_name('quoteText')

while True:
    nextbutton = browser.find_element_by_class_name("next_page")
    nextbutton.click()
    results = browser.find_elements_by_class_name('quoteText')
    try:
      browser.find_element_by_class_name("next_page disabled")
      False
    except:
      True
    for x in results:
        if 'J.K. Rowling' in x.text:
            print (x.text + "\n")
            try:
              browser.find_element_by_class_name("next_page disabled")
              break
              False
            except:
              True
            
    
browser.quit()
