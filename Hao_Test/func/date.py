# 作者：hao.ren3
# 时间：2019/10/11 10:30
# IDE：PyCharm

from re import compile

def is_date_string(date_string):
    """
    :param date_string:
    :return: 判断给定字符串中是否包含日期xxxx-xx-xx
    """
    pattern = compile("[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}")
    result = pattern.match(date_string)
    if result:
        return str(result.group(0))
    else:
        return None
