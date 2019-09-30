# 作者：hao.ren3
# 时间：2019/9/30 11:10
# IDE：PyCharm

from python_scraping.Hao_Test.tools.scrapt_web import get_web_content_and_decode

link = "https://blog.csdn.net/lrenjun/article/details/40862155"
web_content = get_web_content_and_decode(link)
print(web_content)