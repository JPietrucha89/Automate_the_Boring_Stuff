import webbrowser, requests, bs4
from selenium import webdriver
from selenium.webdriver.common.by import By # https://selenium-python.readthedocs.io/locating-elements.html#locating-elements

PATH='D:\Kodzenie\chromedriver.exe' # need to download chromedriver from Chrome's site: https://chromedriver.chromium.org/downloads
games_list=['Rebelia','Root','Scythe']

def check_games_prices_alePlanszowki(games_list):
    URL='https://aleplanszowki.pl/'
    browser.get(URL)
    for game in games_list:
        elemSearch=browser.find_element(By.ID, 'search_query_mobile_bar')
        elemSearch.send_keys(game)
        elemSearch.submit()
        # TODO: tutaj wlasciwe przeszukanie strony z wynikami, znalezienie prawidlowego produktu i pobranie ceny
        pass # placeholder
        # wyczyszczenie searchBoxa
        elemSearch=browser.find_element(By.ID, 'search_query_mobile_bar')
        elemSearch.clear()


#main, warto rozwazyc jeszcze planszove.pl
browser= webdriver.Chrome(PATH)

check_games_prices_alePlanszowki(games_list)

browser.quit()