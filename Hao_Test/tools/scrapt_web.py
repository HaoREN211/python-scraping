# 作者：hao.ren3
# 时间：2019/9/26 13:41
# IDE：PyCharm

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import string
import re

def get_web_content(url):
    """
    :param url:
    :return: 给定url，返回该url里的内容
    """
    # url中包含中文，需要进行转换
    current_page = quote(url, safe=string.printable)
    html = urlopen(current_page)
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