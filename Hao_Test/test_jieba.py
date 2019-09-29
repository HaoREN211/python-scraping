# 作者：hao.ren3
# 时间：2019/9/29 10:08
# IDE：PyCharm

from python_scraping.Hao_Test.tools.sql import create_mysql_connection
from python_scraping.Hao_Test.word.about_word import jieba_cut, calculate_tf_matrix, calculate_list_idf, calculate_matrix_tf_idf
import pandas as pd
import numpy as np

# list_words = pd.read_csv(r'C:\Data\list_words.csv', header=0).word
# list_sentences = pd.read_csv(r'C:\Data\list_sentences.csv', header=0).sentence
# nb_word = pd.read_csv(r'C:\Data\nb_word.csv', header=0).nb_word
# matrix_tf = pd.read_csv(r'C:\Data\matrix_tf.csv', header=0)
# matrix_tf = matrix_tf.values
# list_idf = calculate_list_idf(matrix_tf)


matrix_tf_idf = pd.read_csv(r'C:\Data\matrix_tf_idf.csv', header=0)
matrix_tf_idf = matrix_tf_idf.values
nb_row, nb_column = np.shape(matrix_tf_idf)

list_object_first = list([])
list_object_second = list([])
list_distance = list([])

for first_object in range(nb_row):
    for second_object in range(first_object+1, nb_row, 1):
        distance = 0
        for current_column in range(nb_column):
            distance = distance + pow(matrix_tf_idf[first_object, current_column]-matrix_tf_idf[second_object, current_column], 2)
        distance = np.sqrt(distance)
        list_object_first.append(first_object)
        list_object_second.append(second_object)
        list_distance.append(distance)
result = pd.DataFrame({'first_object': list_object_first, 'second_object': list_object_second, 'distance': list_distance})
print(result)


# 建立数据库连接 获取新闻的标题数据
# mysql_conn = create_mysql_connection("web_crawler")
# cursor = mysql_conn.cursor()
# sql = "select article from news"
# cursor.execute(sql)
# list_sentences = cursor.fetchall()
# cursor.close()
# mysql_conn.close()

# list_words, nb_word = jieba_cut(list_sentences)
# list_sentences = pd.DataFrame({'sentence': list_sentences})
# list_words = pd.DataFrame({"word": list_words})
# nb_word = pd.DataFrame({"nb_word": nb_word})

# nb_word.to_csv(r'C:\Data\nb_word.csv', encoding='utf_8_sig', index=None)
# list_sentences.to_csv(r'C:\Data\list_sentences.csv', encoding='utf_8_sig', index=None)
# list_words.to_csv(r'C:\Data\list_words.csv', encoding='utf_8_sig', index=None)

# print(len(list_sentences))
# print(len(list_words))
# print(len(nb_word))
# print(nb_word)
#
# matrix_tf = calculate_tf_matrix(list_sentences, list_words, nb_word)
# # # print(matrix_tf)
# matrix_tf = pd.DataFrame(matrix_tf)
# matrix_tf.to_csv(r'C:\Data\matrix_tf.csv', index=0)

# matrix_tf_idf = calculate_matrix_tf_idf(matrix_tf, list_idf)
# matrix_tf_idf = pd.DataFrame(matrix_tf_idf)
# matrix_tf_idf.to_csv(r'C:\Data\matrix_tf_idf.csv', index=0)

