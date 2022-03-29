from email import message
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from selenium import webdriver
import random
from time import sleep
from selenium.webdriver.common.by import By
import schedule

def porn():
    # テスト処理
    chromedriver_path = 'chromedriver.exe'

    # PornHub処理
    driver_path = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #chromedriverパス
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
    # chromedriverパス
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get("https://www.deepl.com/ja/translator")
    driver.find_element_by_xpath("/html/body/div[3]/main/div[3]/div[3]/section[1]/div[3]/div[2]/textarea").send_keys(random_title)
    sleep(10)
    output_word = driver.find_element_by_xpath("/html/body/div[3]/main/div[3]/div[3]/section[2]/div[3]/div[1]/textarea").get_attribute("value")

    send_contents = f"【--今日のおすすめ動画--】\r\n\r\n 「{output_word}」\r\n\r\n({random_title})\r\n\r\n {random_url}"
    # LINE_bot処理

    CHANNEL_ACCESS_TOKEN = 'チャンネルアクセストークン'
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

    USER_ID = 'ユーザーID'
    messages = TextSendMessage(text=send_contents)
    line_bot_api.push_message(USER_ID, messages=messages)

schedule.every().day.at('21:00').do(porn)
schedule.every().day.at('13:00').do(porn)

while True:
    schedule.run_pending()
    sleep(1)
