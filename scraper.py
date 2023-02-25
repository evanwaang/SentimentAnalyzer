from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import csv

# Create driver instance, using Firefox, fuck chrome.
driver = webdriver.Firefox()

# Navigating to twitter using get method
driver.get("https://twitter.com/search?q=%20f&src=typed_query")

# Checking if twitter is in the driver title
assert "Twitter" in driver.title

# Wait for the pop-up to appear
not_now_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="Not now"]')))

# Close the pop-up window
not_now_button.click()

# Go to advanced search
advanced_search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//span[text()='Advanced search']/parent::div")))
advanced_search_button.click()

# Input Hastag

these_hashtags = driver.find_element("xpath", "//input[@name='theseHashtags']")
these_hashtags.click()
these_hashtags.send_keys('hello')

# Click search

search_button = driver.find_element(
    "xpath", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/span/span")
search_button.click()

# Click latest

latest_button = driver.find_element(
    "xpath", "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a")
latest_button.click()

# Define the regular expressions for links and hashtags
link_pattern = re.compile(r"http\S+")
hashtag_pattern = re.compile(r"#\w+")

# Define the maximum number of tweets to scrape
max_tweets = 100

link_pattern = re.compile(r"http\S+")
hashtag_pattern = re.compile(r"#\w+")

# Define an empty list to store the tweet content
tweet_content = []

# Scroll down the page to load more tweets
scroll_pause_time = 1
last_height = driver.execute_script("return document.body.scrollHeight")

while len(tweet_content) < max_tweets:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    # Find all the tweets on the page
    tweets = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))

    # Loop through the tweets and extract the text content
    for tweet in tweets:
        try:
            
            content = tweet.text
            lang = tweet.get_attribute("lang")
            if lang != "en":
              continue
            content = re.sub(link_pattern, "", content)
            content = re.sub(hashtag_pattern, "", content)

            tweet_content.append(content)
        except:
            continue

        if len(tweet_content) >= max_tweets:
            break

with open('tweets.csv', mode='w') as file:
    writer = csv.writer(file)
    for tweet in tweet_content:
        writer.writerow([tweet])

       