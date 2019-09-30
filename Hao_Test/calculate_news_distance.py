# 作者：hao.ren3
# 时间：2019/9/30 10:44
# IDE：PyCharm

from python_scraping.Hao_Test.tools.sql import create_mysql_connection
from python_scraping.Hao_Test.word.about_word import jieba_cut, calculate_tf_matrix, calculate_list_idf, calculate_matrix_tf_idf, calculate_matrix_distance

# 建立数据库连接 获取新闻的标题数据
mysql_conn = create_mysql_connection("web_crawler")
cursor = mysql_conn.cursor()
sql = "select article from news"
cursor.execute(sql)
list_sentences = cursor.fetchall()
cursor.close()
mysql_conn.close()

# jieba分词器进行分词
list_words, nb_word = jieba_cut(list_sentences)

# 计算tf矩阵
matrix_tf = calculate_tf_matrix(list_sentences, list_words, nb_word)

# 计算idf向量
list_idf = calculate_list_idf(matrix_tf)

# 计算tf-idf矩阵
matrix_tf_idf = calculate_matrix_tf_idf(matrix_tf, list_idf)

# 计算tf-idf矩阵中两两文章之间的距离
matrix_distance = calculate_matrix_distance(matrix_tf_idf)
