# 作者：hao.ren3
# 时间：2019/9/27 11:26
# IDE：PyCharm

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

def toutiao_get_page_source_by_id(group_id):
    """
    :param group_id:
    :return: 根据group id获取该网页的新闻内容
    """
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")

    toutiao_link = 'https://www.toutiao.com/group/' + str(group_id)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(toutiao_link)
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "article-content"))
        )
        print(element)
        print(type(element))
        print(element.text)
        sub_bs = BeautifulSoup(driver.page_source, 'html.parser')
        # print(sub_bs)
    finally:
        driver.quit()
    return sub_bs


def toutiao_get_new_hot_list():
    """
    :return: 获取今日头条热点新闻列表
    """
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery");
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")

    toutiao_link = 'https://www.toutiao.com/ch/news_hot/'
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(toutiao_link)

    result_link = list([])
    result_title = list([])

    try:
        element = WebDriverWait(driver, 30).until(
            # EC.presence_of_element_located((By.CLASS_NAME, "item    "))
            EC.presence_of_all_elements_located((By.CLASS_NAME, "link"))
        )

        for current_element in element:
            result_link.append(current_element.get_property('href'))
            result_title.append(current_element.text)
    finally:
        driver.quit()
    result = pd.DataFrame({"link": result_link, "title": result_title})
    return result


