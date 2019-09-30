# 作者：hao.ren3
# 时间：2019/9/26 13:41
# IDE：PyCharm

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import string
import re
from pandas import DataFrame
from sqlalchemy import Table, Column, schema, MetaData, BigInteger, String
from time import localtime, strftime
from python_scraping.Hao_Test.tools.sql import create_mysql_engine
from time import sleep

def get_web_content(url):
    """
    :param url:
    :return: 给定url，返回该url里的内容
    """
    # url中包含中文，需要进行转换
    current_page = quote(url, safe=string.printable)
    html = urlopen(current_page)
    if html.headers.get_content_charset() is None:
        bs = BeautifulSoup(html.read().decode(html.headers.get_content_charset(), 'ignore'), 'html.parser')
    else:
        bs = BeautifulSoup(html.read(), 'html.parser')
    return bs

def get_web_content_item(web_content, target, condition, is_text = True, get_all= False):
    """
    :param get_all:
    :param web_content:bs对象
    :param target:标签名
    :param condition:标签符合的条件
    :param is_text:是否是标签内部的值
    :return: 从bs对象中抓取对应标签的值
    """
    if condition:
        result = web_content.find_all(target, condition)
    else:
        result = web_content.find_all(target)
    final_result = []
    if len(result)>0:
        # 如果不是列表，只取第一个匹配的结果
        if not get_all:
            final_result = result[0]
            if is_text:
                final_result = final_result.get_text()
                if len(result)>0:
                    final_result = delete_all_black(final_result)
        else:
            for current_content in result:
                if is_text:
                    tmp = current_content.get_text()
                    if len(tmp) > 0:
                        tmp = delete_all_black(tmp)
                    final_result.append(tmp)
                else:
                    final_result.append(current_content)
    return final_result

def delete_all_black(string):
    """
    :param string:
    :return: 删除字符串string中所有的空白
    """
    pattern = re.compile("\[[0-9999]+\]")
    result = pattern.sub('', str(string), 10000)
    pattern = re.compile("[\t\r\n ]+")
    result = pattern.sub('', result, 10000)
    result = result.replace(" ", "")
    result = result.replace("　", "")
    return result

def get_liepin_job_link():
    """
    :return:获取猎聘网上所有岗位的链接
    """
    print("---> 正在获取所有岗位的链接")
    url = "https://www.liepin.com/zhaopin/?init=-1&headckid=3e053079b29e4ce9&flushckid=1&fromSearchBtn=2&dqs=280020&pubTime=1&ckid=5e2017eff8c8fe62&sfrom=click-pc_homepage-centre_searchbox-search_new&key=%E4%BC%9A%E8%AE%A1&siTag=yBAlj2NjO-bNRNh2rd-zhw%7EDARaeHgTI7JY9N3sNhM1Ow&d_sfrom=search_fp&d_ckId=dd21085024abcfea7a31cf5ad246d1da&d_curPage=0&d_pageSize=40&d_headId=42d81e285bf9fc398e27eb711e0ea871"
    list_job_link = list([])
    prefix = "https://www.liepin.com"
    while True:
        bs = get_web_content(url)
        job_object_list = bs.find_all('a', href=re.compile('https://www.liepin.com/job/[0-9]+.*'))
        for current_job_object in job_object_list:
            list_job_link.append(current_job_object.attrs['href'])
        next_list_job_page = bs.find_all('a', text='下一页')
        if len(next_list_job_page) > 0:
            if 'javascript' in next_list_job_page[0].attrs['href']:
                break
            url = prefix + "" + next_list_job_page[0].attrs['href']
        else:
            break
    return list_job_link

def find_regular_expression(string, pattern, group):
    """
    :param string:
    :param pattern:
    :param group:
    :return: 正则匹配
    """
    string_pattern = re.compile(pattern)
    result = re.match(string_pattern, string)
    if result is None:
        return ''
    else:
        return result.group(group)

def find_liepin_salary(salaries, unit=False, min_value=True):
    """
    :param salaries:
    :param unit:是否返回工资单位
    :param min_value: 是否返回最小工资，否则就返回最大工资
    :return: 找到最小工资
    """
    salary_pattern = '^([0-9]+)-([0-9]+)([万千]+).+'
    position = 0
    if unit:
        position = 3
    else:
        if min_value:
            position = 1
        else:
            position = 2
    return find_regular_expression(salaries, salary_pattern, position)

def find_liepin_place(location, city=True):
    """
    :param location:
    :param city: True就返回城市，否则返回区域
    :return: 找到猎聘上的城市信息
    """
    if(location==''):
        return ''
    else:
        string_pattern = '^(.+)-(.+)$'
        result = re.match(string_pattern, location)
        if result is None:
            if city==True:
                return location
            else:
                return ''
        else:
            if city==True:
                return result.group(1)
            else:
                return result.group(2)

def get_liepin_job_info(current_job_link):
    """
    :param current_job_link:
    :return: 獲取獵聘網站崗位的詳細信息
    """
    list_title = list([])
    list_company = list([])
    list_salary_min = list([])
    list_salary_max = list([])
    list_salary_unit = list([])
    list_city = list([])
    list_district = list([])
    list_degree = list([])
    list_experience = list([])
    list_language = list([])
    list_age = list([])
    list_link = list([])
    list_origin = list([])
    list_time = list([])
    list_time.append(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    list_origin.append("猎聘")
    bs = get_web_content(current_job_link)
    list_link.append(current_job_link)
    list_title.append(get_web_content_item(bs, 'h1', {}, is_text=True))
    list_company.append(get_web_content_item(bs, 'a', {'data-promid': re.compile('^$')}, is_text=True))
    salary = get_web_content_item(bs, 'p', {'class': 'job-item-title'}, is_text=True)
    list_salary_min.append(find_liepin_salary(salary))
    list_salary_max.append(find_liepin_salary(salary, min_value=False))
    list_salary_unit.append(find_liepin_salary(salary, unit=True))
    location = get_web_content_item(bs, 'p', {'class': 'basic-infor'}, is_text=False)
    city_string = get_web_content_item(location, 'a', {}, is_text=True)
    list_city.append(find_liepin_place(city_string))
    list_district.append(find_liepin_place(city_string, city=False))

    div_profile = get_web_content_item(bs, 'div', {'class': 'job-qualifications'}, is_text=False)
    list_profile = div_profile.find_all('span', {})

    indicator = 0
    degree = experience = language = age = ''
    for current_profile in list_profile:
        if indicator == 0:
            degree = current_profile.get_text()
        elif indicator == 1:
            experience = current_profile.get_text()
        elif indicator == 2:
            language = current_profile.get_text()
        else:
            age = current_profile.get_text()
        indicator += 1
    list_degree.append(degree)
    list_experience.append(experience)
    list_language.append(language)
    list_age.append(age)

    result = DataFrame({"title": list_title,
                        "origin": list_origin,
                        "company": list_company,
                        "salary_min": list_salary_min,
                        "salary_max": list_salary_max,
                        "salary_unit": list_salary_unit,
                        "city": list_city,
                        "district": list_district,
                        "degree": list_degree,
                        "experience": list_experience,
                        "language": list_language,
                        "age": list_age,
                        "link": list_link,
                        "execute_time": list_time})
    return result

def init_liepin_table(mysql_engine):
    """
    :param mysql_engine:
    :return: 存放存储猎聘网站信息的表
    """
    print("---> 初始化猎聘主表")
    jobs = get_liepin_table_script(mysql_engine)
    if not jobs.exists():
        jobs.create()

def get_liepin_table_script(mysql_engine):
    """
    :param mysql_engine:
    :return: 返回创建liepin主表的脚本
    """
    metadata = MetaData(mysql_engine)
    return Table("jobs", metadata,
                 Column("id", BigInteger, primary_key=True, autoincrement=True),
                 Column("title", String(300), comment='岗位名称'),
                 Column("origin", String(20), comment='网站来源'),
                 Column("company", String(100), comment='公司名称'),
                 Column("salary_min", String(20), comment='最低薪资'),
                 Column("salary_max", String(20), comment='最高薪资'),
                 Column("salary_unit", String(20), comment='薪资单位'),
                 Column("city", String(20), comment='城市'),
                 Column("district", String(20), comment='区域'),
                 Column("degree", String(20), comment='学历要求'),
                 Column("experience", String(20), comment='工作年限'),
                 Column("language", String(20), comment='语言要求'),
                 Column("age", String(20), comment='年龄要求'),
                 Column("link", String(20), comment='网站链接'),
                 Column("execute_time", String(20), comment='执行时间'), schema='web_crawler')

def get_all_liepin_info():
    """
    :return:
    """
    list_job_link = get_liepin_job_link()

    my_engine = create_mysql_engine("web_crawler")
    init_liepin_table(my_engine)

    # list_column = ["title",  "origin",  "company",  "salary_min",  "salary_max",  "salary_unit",  "city",  "district",  "degree",  "experience",  "language",  "age",  "link",  "execute_time"]
    # liepins = DataFrame(columns=list_column)
    jobs = get_liepin_table_script(my_engine)
    # 逐条读取岗位的信息
    for current_job_link in list_job_link:
        nb_row = len(jobs.select(jobs.c.link == current_job_link).execute().fetchall())
        if nb_row>0:
            print("---> 已经爬取了%s的内容，跳过此岗位" % current_job_link)
            continue
        print("---> 正在爬取%s" % current_job_link)
        current_dataset = get_liepin_job_info(current_job_link)
        current_dataset.to_sql(name="jobs", con=my_engine, index=False, if_exists="append")
        # liepins = liepins.append(get_liepin_job_info(current_job_link), ignore_index=True)
        sleep(15)
    # 将爬取下来的数据存放到数据库中
    # if not liepins.empty:
    #     liepins.to_sql(name="jobs", con=my_engine, index=False, if_exists="append")
    my_engine.dispose()
