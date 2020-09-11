import requests
from bs4  import BeautifulSoup
from selenium import webdriver
import urllib
import random
import time
import schedule
import subprocess




def steal():

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options=options)


    driver.get("https://www.instagram.com/beastrwa/")

    body = driver.find_element_by_tag_name("body")
    page = body.get_attribute("innerHTML")


    soup = BeautifulSoup(page, "html.parser")


    user_image_tag = soup.select('.be6sR')

    current_url = open('url', 'r+')
    new_image_url = user_image_tag[0]["src"]


    image_name = random.randrange(1,100000000000000)


    if current_url.read() != new_image_url:


        current_url.write(user_image_tag[0]["src"])
        current_url.close()
        driver.get('https://www.instadp.com/fullsize/beastrwa')
        body = driver.find_element_by_tag_name("body")
        page = body.get_attribute("innerHTML")
        soup = BeautifulSoup(page, "html.parser")
        user_image_tag = soup.select('.picture')
        new_image_url = user_image_tag[0]["src"]
        urllib.request.urlretrieve(new_image_url, f"{image_name}.jpg")

    else:
        print("Image is already downloaded")
        
        

    # print(pre_image_url.read())
    # print(new_image_url)

    driver.close()


schedule.every(10).seconds.do(steal)

while True:
    schedule.run_pending()
    time.sleep(1)