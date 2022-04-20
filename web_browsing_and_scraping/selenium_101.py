from selenium import webdriver
PATH='D:\Kodzenie\chromedriver.exe'

browser= webdriver.Chrome(PATH)
browser.get('https://aleplanszowki.pl/')

# look for first element matching given css selector
elem= browser.find_element_by_css_selector('#st_banner_block_21')
##st_banner_block_21 to Gry Uszkodzone
elem.click()

# look for all elements matching given css selector
elems=browser.find_elements_by_css_selector('p')
print(len(elems))

browser.back()

# look for search inputBox and pass string argument to it, then click button Search
elemSearch= browser.find_element_by_css_selector('#search_query_mobile_bar')
elemSearch.send_keys('Rebelia') # type string into search bar
elemSearch.submit() # same as clicking Search button

browser.back()
browser.forward()
browser.refresh()
browser.quit()