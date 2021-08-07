import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from langdetect import detect
from icecream import ic

opts = ChromeOptions()
opts.headless = False
assert opts.headless == False
browser = Chrome(options=opts)
browser.get('https://www.goodreads.com/quotes/tag/harry-potter?page=1')
results = browser.find_elements_by_class_name('quoteText')
#Note to self fix the exceptions here at some point, I had a version of this that definitely checked exceptions properly

while True:
    nextbutton = browser.find_element_by_class_name("next_page")
    nextbutton.click()
    results = browser.find_elements_by_class_name('quoteText')
    ic(len(results))

    for x in results:
        if 'J.K. Rowling' in x.text:
            print (x.text + "\n")
    try:
        browser.find_element_by_css_selector("body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(20) > div > span.next_page.disabled") 
        browser.quit()     
    except:
          True
    
browser.quit()
