from langdetect.detector_factory import detect_langs
import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from langdetect import detect
from icecream import ic
import re

opts = ChromeOptions()
opts.headless = False
assert opts.headless == False
browser = Chrome(options=opts)
browser.get('https://www.goodreads.com/quotes/tag/harry-potter?page=1')
results = browser.find_elements_by_class_name('quoteText')
#Note to self fix the exceptions here at some point, I had a version of this that definitely checked exceptions properly
#Okay so now what I need to do is get it to filter
#Also get it to write
#This needs to be a function

with open('./fortunefile', 'w') as f:

    while True:
        nextbutton = browser.find_element_by_class_name("next_page")
        nextbutton.click()
        results = browser.find_elements_by_class_name('quoteText')
        ic(len(results))
        
        for x in results:
            if 'J.K. Rowling' in x.text and detect(x.text) == 'en':
                y = re.sub(r"J.K. Rowling,?",'',x.text,flags=re.IGNORECASE)
                f.write(y + "\n")
                f.write("%")
                f.write("\n")
        try:
            browser.find_element_by_css_selector("body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(20) > div > span.next_page.disabled") 
            f.closed
            browser.quit()     
        except:
            True