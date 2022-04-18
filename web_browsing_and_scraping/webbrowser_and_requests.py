import webbrowser
import requests
import os

# open given URL in default browser
URL='https://www.google.pl/maps/preview'
#webbrowser.open(URL)

file_URL='https://automatetheboringstuff.com/files/rj.txt'
res=requests.get(file_URL) # create and return response object

print(res.status_code) # status_code - 200 means everything is in order
res.raise_for_status() # raises an exception if status_code != 200
if res.status_code == requests.codes.ok: # another way to check if request's status code is fine 
    print(len(res.text))

    os.chdir('web_browsing_and_scraping')
    playFile=open('RomeoAndJuliet.txt','wb') # write binary

# The iter_content() method returns “chunks” of the content on each iteration through the loop. Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so pass 100000 as the argument to iter_content().
    for chunk in res.iter_content(100000):
        playFile.write(chunk) # write out whole res.text to playFile
    playFile.close