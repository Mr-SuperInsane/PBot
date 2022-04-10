from selenium import webdriver
import deepl
import random

heroku_driver = '/app/.chromedriver/bin/chromedriver'

def pornhub():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #chromedriverパス
    driver = webdriver.Chrome(heroku_driver, options=options)
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
    return output_word, random_title, random_url


def xvideos():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #chromedriverパス
    driver = webdriver.Chrome(heroku_driver, options=options)
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
    translator = deepl.Translator('602efc52-a29d-d7a6-7613-1277095e4fb3:fx')
    output_word = translator.translate_text(random_title,target_lang='JA')
    return output_word, random_title, random_url

def spankbang():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #chromedriverパス
    driver = webdriver.Chrome(heroku_driver, options=options)
    driver.get("https://jp.spankbang.com/trending_videos/")
    videos_title = []
    videos_url = []
    for n in range(16):
        if n < 6:
            pass
        else:
            xpath = f'/html/body/main/div[1]/div/div/div[1]/div[{n}]/a[2]'
            video = driver.find_element_by_xpath(xpath)
            videos_title.append(video.text)
            videos_url.append(video.get_attribute("href"))
            print(video.text, video.get_attribute('href'))
    driver.quit()
    video = dict(zip(videos_title,videos_url))
    random_title = random.choice(videos_title)
    random_url = video[random_title]
    translator = deepl.Translator('602efc52-a29d-d7a6-7613-1277095e4fb3:fx')
    output_word = translator.translate_text(random_title,target_lang='JA')
    return output_word, random_title, random_url
