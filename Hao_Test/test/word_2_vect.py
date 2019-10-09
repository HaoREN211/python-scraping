# 作者：hao.ren3
# 时间：2019/10/8 17:49
# IDE：PyCharm

if __name__ == '__main__':
    from sqlalchemy import Table, MetaData, Integer, Text, Column
    from python_scraping.Hao_Test.tools.sql import create_mysql_engine
    from python_scraping.Hao_Test.word.about_word import jieba_cut
    from gensim.models import Word2Vec

    my_engine = create_mysql_engine("web_crawler")
    meta_data = MetaData(my_engine)
    news_table = Table("news", meta_data,
                       Column('id', Integer, primary_key=True, autoincrement=True),
                       Column('article', Text))

    data = news_table.select(news_table.c.id == 1).execute().fetchone()
    article = data[1]

    list_words = jieba_cut(article)
    model = Word2Vec(list_words, size=100, window=10, min_count=3)

    my_engine.dispose()
