import icecream
from langdetect.detector_factory import detect_langs
import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from langdetect import detect
from icecream import ic
import re
import click

opts = ChromeOptions()
opts.headless = False
assert opts.headless == False
browser = Chrome(options=opts)
browser.get('https://goodreads.com')
results = browser.find_elements_by_class_name('quoteText')
#Note to self fix the exceptions here at some point, I had a version of this that definitely checked exceptions properly
#Okay so now what I need to do is get it to filter
#Also get it to write
#This needs to be a function
#So here's how it works
#Next: Language Choice
#Next Compile multiple into one

#The person searches for a novel. If that novel has spaces in it we're going to want to filter those out 
#We look with this URL https://www.goodreads.com/quotes/tag/#{ThingHere}
#We're going to have to Search in order to find the author 
#Perhaps we should check the author
#Then we're going to runthrough main 

#The UI 
@click.command()
@click.argument('book')
def search(book):
    x = book
    x = re.sub(r" ",'-',x)
    ic(book)
    author(book)

def author(book):
    searchbar = browser.find_element_by_id('sitesearch_field')
    searchbar.send_keys(book)
    searchform = browser.find_element_by_class_name("submitLink")
    searchform.submit()
    temp = browser.find_elements_by_class_name('bookTitle')
    ic(temp)
    titleresults = []
    for i in temp:
        ic(i.text)
        titleresults.append(i.text)
    ic(titleresults)
    authorresults = browser.find_elements_by_class_name('authorName')
    
    #So the thing we've reached here is that we have these two collections of elements and want to make those telements into a key value pair 
    booksandauthors = dict(zip(titleresults,authorresults))
    for i in booksandauthors.keys():
        print(i, booksandauthors.values[i])
        if click.confirm('Is the above your book?'):
            #Call the main function
            BibliothecaVerbum()
            pass
        

def main():
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

if __name__ == '__main__':
    search()