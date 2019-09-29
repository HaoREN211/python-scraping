# 作者：hao.ren3
# 时间：2019/9/27 15:53
# IDE：PyCharm

import re
import time

from python_scraping.Hao_Test.tools.scrapt_web import delete_all_black
from python_scraping.Hao_Test.tools.scrapt_web import get_web_content
from python_scraping.Hao_Test.tools.scrapt_web import get_web_content_item
from python_scraping.Hao_Test.tools.sql import create_mysql_connection

def get_sina_news_content(link):
    """
    :param link:
    :return: 给定新浪新闻的链接，获取链接里的内容
    """
    print("---> 正在获取内容：%s" % link)
    web_content = get_web_content(link)
    title = get_web_content_item(web_content, 'h1', {'class': 'main-title'})
    article = get_web_content_item(web_content, 'div', {'class': 'article'}, is_text=False)
    article_p = article.find_all('p')
    list_content = []
    for i in article_p:
        if not i.has_attr('class'):
            if (not '原标题：' in i.get_text()) and (not '来源：' in i.get_text()):
                if len(i.find_all('strong')) == 0:
                    list_content.append(i.get_text())
    content = ''.join(list_content)
    content = delete_all_black(content)
    result = {'title': title, 'article': content, 'link': link, 'origin': '新浪新闻', 'plate': '国内'}
    return result


def get_sina_list_news(platform):
    """
    :param platform:
    :return:返回新浪某个板块内的新闻列表
    """
    # url = "https://news.sina.com.cn/china/"
    url = "https://news.sina.com.cn/"+platform
    content = get_web_content(url)
    list_block = get_web_content_item(content, 'ul', condition={}, is_text=False, get_all=True)
    pattern = re.compile("https://news.sina.com.cn/c/"+str(time.strftime("%Y-%m-%d", time.localtime()))+"/.*")
    list_link = list([])
    for current_ul in list_block:
        list_current_link = get_web_content_item(current_ul, 'a', {"href": pattern}, is_text=False, get_all=True)
        for link in list_current_link:
            list_link.append(link["href"])
    list_link = list(set(list_link))
    return list_link

def get_sina_chinese_news():
    """
    :return: 获取国内新闻的内容
    """
    init_mysql()
    list_news = get_sina_list_news("china")
    result = list([])
    for current_news in list_news:
        result.append(get_sina_news_content(current_news))
    store_into_database(result)


def init_mysql():
    """
    :return:初始化存放数据的数据库和数据表
    """
    mysql = create_mysql_connection("mysql")
    mysql_cursor = mysql.cursor()

    mysql_cursor.execute("create database IF NOT EXISTS web_crawler DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
    mysql_cursor.execute("""create table if not exists web_crawler.news (
      id int PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
      title VARCHAR(300) COMMENT '标题',
      date TIMESTAMP COMMENT '获取时间',
      origin VARCHAR(20) COMMENT '新闻来源',
      plate VARCHAR(20) COMMENT '板块',
      link VARCHAR(300) COMMENT '链接',
      article TEXT COMMENT '内容')""")

    mysql_cursor.close()
    mysql.close()

def store_into_database(result):
    has_one_data = False
    mysql = create_mysql_connection("web_crawler")
    mysql_cursor = mysql.cursor()
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    sql_multiple = "INSERT INTO `news`(`title`, `date`, `origin`, `plate`, `link`, `article`) VALUES "
    for current_result in result:
        if not find_if_news_exist(current_result['link'], mysql_cursor):
            print("---> 正在存储：" + current_result['title'])
            if not has_one_data:
                has_one_data = True
            else:
                sql_multiple = sql_multiple + ", "
            sql_multiple = sql_multiple + """('"""+replace_quotes(current_result['title'])+"""','"""+\
                           local_time+"""','"""+replace_quotes(current_result['origin'])+"""',
                '"""+replace_quotes(current_result['plate'])+"""','"""+replace_quotes(current_result['link'])+\
                """','"""+replace_quotes(current_result['article'])+"""')"""
    if has_one_data:
        sql_multiple = sql_multiple + ";"
        mysql_cursor.execute(sql_multiple)
        mysql.commit()

    mysql_cursor.close()
    mysql.close()

def find_if_news_exist(link, sql_cursor):
    """
    :param link:
    :param sql_cursor:
    :return:根据新闻的链接判断数据库中当前是否已经包含了该新闻
    """
    sql = "SELECT id FROM `news` WHERE link = '"+link+"'"
    sql_cursor.execute(sql)
    results = sql_cursor.fetchall()
    if len(results) > 0:
        return True
    else:
        return False

def replace_quotes(text):
    return str(text).replace("'", "\"")
