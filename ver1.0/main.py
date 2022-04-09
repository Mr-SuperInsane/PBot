from linebot import LineBotApi
from linebot.models import TextSendMessage
from selenium import webdriver
import random
import schedule
import deepl
from time import sleep

# PornHub処理
def pornhub():
    driver_path = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #chromedriverパス
    driver = webdriver.Chrome(driver_path, options=options)
    driver.get("https://jp.pornhub.com/recommended")

    videos_title = []
    videos_url = []

    for n in range(5):
        n += 2
        #/html/body/div[3]/div[2]/div[3]/div[1]/div[3]/ul/li[3]/div/div[5]/span/a
        xpath = f"/html/body/div[3]/div[2]/div[3]/div[1]/div[3]/ul/li[{n}]/div/div[5]/span/a"
        video = driver.find_element_by_xpath(xpath)
        videos_title.append(video.text)
        videos_url.append(video.get_attribute("href"))
    driver.quit()
    video_dict = dict(zip(videos_title,videos_url))
    random_title = random.choice(videos_title)
    random_url = video_dict[random_title]
    # DeepL 処理
    # chromedriverパス
    translator = deepl.Translator('602efc52-a29d-d7a6-7613-1277095e4fb3:fx')
    output_word = translator.translate_text(random_title,target_lang='JA')
    message = f'【今日のおすすめ動画】\r\n\r\n『{output_word}』\r\n\r\n\n({random_title})\r\n\r\n{random_url}'

    line_bot_api = LineBotApi('チャンネルアクセストークン')
    line_bot_api.broadcast(TextSendMessage(text=message))

schedule.every().day.at("13:00").do(pornhub)
while True:
    schedule.run_pending()
    sleep(1)
