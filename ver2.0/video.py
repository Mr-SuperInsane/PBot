from selenium import webdriver
import deepl
import random
import pycld2 as cld2
# 開発用モジュール
from webdriver_manager.chrome import ChromeDriverManager

driver_path = '/app/.chromedriver/bin/chromedriver'

def pornhub():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #chromedriverパス
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
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
    check = 'true'
    output_word = random_title
    isReliable, textBytesFound, detail = cld2.detect(random_title)
    if detail[0][1] != 'ja':
        translator = deepl.Translator('AuthKey')
        output_word = translator.translate_text(random_title,target_lang='JA')
        check = 'false'
    return output_word, random_title, random_url, check


def xvideos():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #chromedriverパス
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://www.xvideos.com/best")
    videos_title = []
    videos_url = []
    for n in range(10):
        n+=1
        xpath = f'/html/body/div/div[4]/div[3]/div/div[{n}]/div[2]/p[1]/a'
        video = driver.find_element_by_xpath(xpath)
        videos_title.append(video.text)
        videos_url.append(video.get_attribute("href"))
    driver.quit()
    video = dict(zip(videos_title,videos_url))
    random_title = random.choice(videos_title)
    random_url = video[random_title]
    check = 'true'
    output_word = random_title
    isReliable, textBytesFound, detail = cld2.detect(random_title)
    if detail[0][1] != 'ja':
        translator = deepl.Translator('AuthKey')
        output_word = translator.translate_text(random_title,target_lang='JA')
        check = 'false'
    return output_word, random_title, random_url, check

def xhamster():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #chromedriverパス
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://jp.xhamster.com/best")
    videos_title = []
    videos_url = []
    for n in range(10):
        if n == 0:
            n+=2
        elif n==1:
            pass
        else:
            n+=1
        xpath = f'/html/body/div[1]/main/div/article/div[2]/div/div[{n}]/div/a'
        video = driver.find_element_by_xpath(xpath)
        videos_title.append(video.text)
        videos_url.append(video.get_attribute("href"))
    driver.quit()
    video = dict(zip(videos_title,videos_url))
    random_title = random.choice(videos_title)
    random_url = video[random_title]
    check = 'true'
    output_word = random_title
    isReliable, textBytesFound, detail = cld2.detect(random_title)
    if detail[0][1] != 'ja':
        translator = deepl.Translator('AuthKey')
        output_word = translator.translate_text(random_title,target_lang='JA')
        check = 'false'
    return output_word, random_title, random_url, check
