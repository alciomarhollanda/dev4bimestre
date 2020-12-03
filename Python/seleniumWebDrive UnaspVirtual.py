import time
from selenium import webdriver # pip install selenium

"""
Olá 3TI
"""

# Optional argument, if not specified will search path.
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://unasp.mrooms.net/')
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('username')
search_box.send_keys('ht.0037720')
search_box = driver.find_element_by_name('password')
search_box.send_keys('0037720')
# search_box.submit()
time.sleep(50)  # Let the user actually see something!
# driver.quit()
