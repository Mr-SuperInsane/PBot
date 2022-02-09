from flask import request
from selenium import webdriver
from selenium.webdriver.common.by import By
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import requests
import random
from time import sleep
import schedule

#schedule 処理
def porn():
    #selenium処理
    driver_path = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get("https://jp.pornhub.com/recommended")

    videos_title = []
    videos_url = []

    for n in range(20):
        n += 2
        xpath = "/html/body/div[3]/div[2]/div[3]/div[1]/div[3]/ul" + "/li[{}]/div/div[5]/span/a".format(n)
        video = driver.find_element(by=By.XPATH, value=xpath)
        videos_title.append(video.text)
        videos_url.append(video.get_attribute("href"))

    driver.quit()
    video_dict = dict(zip(videos_title,videos_url))
    random_title = random.choice(videos_title)
    random_url = video_dict[random_title]

    # DeepL 処理
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get("https://www.deepl.com/ja/translator")
    driver.find_element_by_xpath("/html/body/div[3]/main/div[3]/div[3]/section[1]/div[2]/div[2]/textarea").send_keys(random_title)
    sleep(10)
    output_word = driver.find_element_by_xpath("/html/body/div[3]/main/div[3]/div[3]/section[2]/div[3]/div[1]/textarea").get_attribute("value")

    # LINE nortify処理
    TOKEN = "9XWjMfjnhVXB7snWRlNboVETvQwXYi468Uy0lyPU2YH"
    api_url = "https://notify-api.line.me/api/notify"

    send_contents = f"\r\n【--今日のおすすめ--】\r\n\r\n 「{output_word}」\r\n\r\n({random_title})\r\n\r\n 「{random_url}」"
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {"message":send_contents}
    requests.post(api_url, headers=TOKEN_dic, data=send_dic)

schedule.every().day.at("13:00").do(porn)
while True:
    schedule.run_pending()
    sleep(1)