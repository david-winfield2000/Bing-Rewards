import webbrowser
import string
import random
import os
import time

time.sleep(30)

edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge))

for i in range(31):
    letters = string.ascii_lowercase
    query = ''.join(random.choice(letters) for i in range(10))
    webbrowser.get('edge').open('https://www.bing.com/search?q=' + query)

time.sleep(10)

os.system("taskkill /im msedge.exe")