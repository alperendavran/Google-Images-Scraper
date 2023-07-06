import os
import base64
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# function converting query to intended google images URL
def url(query):
    return "https://www.google.com/search?q=" + query + "&tbm=isch"

DRIVER_PATH = '/Users/alperendavran/Downloads/chromedriver_mac_arm64 (2)/chromedriver'
SAVE_FOLDER = '/Users/alperendavran/Desktop/mountain images'

# create a new instance of the Chrome driver
service = Service(DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=service, options=options)

# search queries list, each of their images will be accessed 
search_queries = [
    "Mount Everest","Sagarmatha","Chomolungma","K2","Kangchenjunga",
    "Lhotse","Makalu","Cho Oyu","Dhaulagiri I","Manaslu","Nanga Parbat",
    "Annapurna I"
]

# construct list of complete URLs
complete_urls = [url(query) for query in search_queries]

MAX_RETRIES = 3  # Maximum number of retries for each URL this will eliminate cases in case of network error or some connection problmes etc.

# iterate over the complete URLs
for idx, search_url in enumerate(complete_urls):
    for attempt in range(MAX_RETRIES):
        try:
            print(f"Processing {search_url}...")
            driver.get(search_url)

            # wait for the images to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rg_i.Q4LuWd")))

            image = driver.find_element(By.CSS_SELECTOR, '.rg_i.Q4LuWd')  # find the image element
            my_image = image.get_attribute('src').split('data:image/jpeg;base64,') # split its base64 format and get src feature
            filename = os.path.join(SAVE_FOLDER, search_queries[idx] + '.jpeg') #In this line filename in which the image to be downloaded is saved is specified 
           
            if len(my_image) > 1:  #that means image in base64 format 
                print(f"Writing file {filename}...")
                with open(filename, 'wb') as f:
                    f.write(base64.b64decode(my_image[1]))
            else: #otherwise, image will be downloaded directly from URL
                print(f"Retrieving image from {image.get_attribute('src')}...")
                urllib.request.urlretrieve(image.get_attribute('src'), filename)

            # Successful, so break out of the loop for retries
            break

        except Exception as e:
            print(f"Error with {search_url} on attempt {attempt + 1} of {MAX_RETRIES}: {e}")   
        else:
            print(f"Successfully processed {search_url}!")
    else:  # Only reached if the for loop completed without a break, meaning all attempts failed
        print(f"Failed to process {search_url} after {MAX_RETRIES} attempts.")

# close the browser
try:
    driver.quit()
except Exception as e:
    print(f"Error quitting the driver: {e}")
else:
    print("Successfully quit the driver.")