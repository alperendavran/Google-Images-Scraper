# Google-Images-Scraper

This python program is a simple, yet effective Google Images scraper. It's designed to automate the process of downloading images from Google by searching a list of queries and saving the first returned image for each query. It is based on Selenium, a powerful tool for controlling a web browser through the program.

#Prerequisites
Python 3.6 or higher.
Selenium WebDriver and related packages (install via pip install selenium).
urllib and base64 libraries (standard in Python 3.x).
Google Chrome installed on your machine.
Chromedriver executable that matches your installed Chrome version and your machine's OS (download from here).

#Setup
Place the chromedriver executable in a known location on your machine.
Update the DRIVER_PATH in the script to the path where chromedriver is located.
Update the SAVE_FOLDER with the path where you want to store the downloaded images.

#Usage
The script accepts a list of search queries in the search_queries list. These queries are then fed to Google Images, the script navigates to each link, and the first image from each search result is downloaded.

Images are saved to the specified SAVE_FOLDER in JPEG format. Each file's name will be the same as the corresponding search query. If there are any problems accessing an URL (e.g., due to network issues), the script will attempt to retry a set number of times (defined by MAX_RETRIES).

After all URLs are processed, the web browser controlled by Selenium will be closed.

#Limitations & Disclaimer
This script does not evade Google's anti-bot measures. If Google detects that an automated script is downloading images, it may temporarily block your IP. Also, this script doesn't account for the "Show more results" button on Google Images; it will only download the first visible image.

Remember that using this script may infringe on copyrights and/or Google's Terms of Service. The user is responsible for any issues that arise from such infringement.

#Contributing
This script is open to improvements. If you experience any issues or have any feature requests, please open an issue or a pull request.

#License
This project is licensed under the terms of the MIT license.
