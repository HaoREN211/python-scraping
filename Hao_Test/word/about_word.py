# 作者：hao.ren3
# 时间：2019/9/29 11:53
# IDE：PyCharm

from os.path import join
from os import walk
import pandas as pd
import jieba
import numpy as np
from math import ceil, log

def get_useful_word():
    """http://thuocl.thunlp.org/sendMessage 清华大学开放中文词库
    :return: 获取清华大学词库
    """
    folder = r'C:\Users\hao.ren3\AppData\Local\Programs\Python\Python37\Scripts\Jupyter\python_scraping\Hao_Test\word\useful'
    g = walk(folder)
    list_word = list([])
    for path,dir_list,file_list in g:
        for current_file in file_list:
            if not 'txt' in current_file:
                continue
            current_file_path = join(folder, current_file)
            print("---> 加载%s文件里的词库" % current_file)
            data = pd.read_csv(current_file_path, header=None, sep="\t")
            list_word.extend(data.iloc[:, 0])
    list_word = list(set(list_word))
    return list_word


def get_stop_list_word():
    """https://github.com/goto456/stopwords 中文常用停用词表
    :return:获取停用词库
    """
    folder = r'C:\Users\hao.ren3\AppData\Local\Programs\Python\Python37\Scripts\Jupyter\python_scraping\Hao_Test\word\stoplist'
    g = walk(folder)
    list_word = list([])
    for path, dir_list, file_list in g:
        for current_file in file_list:
            if not 'txt' in current_file:
                continue
            current_file_path = join(folder, current_file)
            print("---> 加载%s文件里的停用词库" % current_file)
            data = pd.read_csv(current_file_path, header=None, sep="\n")
            list_word.extend(data.iloc[:, 0])
    list_word = list(set(list_word))
    return list_word

def jieba_cut(list_sentences):
    """
    :param list_sentences:
    :return: 将句子通过jieba分词器进行分词，并考虑到了停用词和常用词
    """
    list_ciyu = list([])

    # 创建停用词词库
    list_stop_word = list(map(lambda x: str(x).strip(), get_stop_list_word()))

    # 创建常用词词库
    list_word = list(map(lambda x: str(x).strip(), get_useful_word()))
    for current_word in list_word:
        jieba.add_word(current_word)

    nb_word = list([])

    # 将各个新闻的标题拆分成词语
    for current_title in list_sentences:
        current_list_word = list([])
        list_title_word = jieba.cut(current_title[0], cut_all=False)
        for current_title_word in list_title_word:
            target = str(current_title_word).strip()
            if len(target) < 2:
                continue
            if not target in list_stop_word:
                list_ciyu.append(target)
                current_list_word.append(target)
        current_list_word = list(set(current_list_word))
        nb_word.append(len(current_list_word))

    # 将拆分出来的词语通过停用词词库过滤，只留下有价值的词语
    list_ciyu = list(set(list_ciyu))
    return list_ciyu, nb_word

def calculate_tf_matrix(list_sentences, list_words, nb_word):
    """
    :param list_sentences:
    :param list_words:
    :param nb_word:
    :return: 计算tf矩阵
    """
    print("---> 获取tf矩阵")
    matrix_tf = np.zeros((len(list_sentences), len(list_words)))
    index_sentence = -1
    for current_sentence in list_sentences:
        index_sentence = index_sentence + 1
        current_sentence_length = nb_word[index_sentence]
        if current_sentence_length == 0:
            continue
        index_word = 0
        for current_word in list_words:
            current_tf = str(current_sentence).count(str(current_word))
            current_tf_normalized = ceil(current_tf * 100 / current_sentence_length)
            matrix_tf[index_sentence, index_word] = current_tf_normalized
            index_word = index_word + 1
    return matrix_tf

def calculate_list_idf(matrix_tf):
    """
    :param matrix_tf:log(语料库的文档总数除以包含该词的文档数加1)
    :return: 根据tf矩阵计算idf列表
    """
    print("---> 获取idf向量")
    nb_row, nb_column = np.shape(matrix_tf)
    list_idf = [0] * nb_column
    print(nb_row)
    for current_column in range(nb_column):
        row_has_data = 0
        for current_row in range(nb_row):
            if matrix_tf[current_row, current_column] > 0:
                row_has_data = row_has_data + 1
        current_idf = log(nb_row * 1.0 / (row_has_data + 1))
        list_idf[current_column] = current_idf
    # 归一化
    idf_max = max(list_idf)
    idf_min = min(list_idf)
    list_idf = list(map(lambda x: (x - idf_min) * 1.0 / (idf_max - idf_min), list_idf))
    return list_idf

def calculate_matrix_tf_idf(matrix_tf, list_idf):
    """
    :param matrix_tf:
    :param list_idf:
    :return:根据tf矩阵和idf向量计算tf-idf矩阵
    """
    print("---> 获取tf-idf矩阵")
    tf_max = np.max(matrix_tf)
    tf_min = np.min(matrix_tf)
    matrix_tf = (matrix_tf - tf_min) * 1.0 / (tf_max - tf_min)
    nb_row, nb_column = np.shape(matrix_tf)
    matrix_tf_idf = np.zeros((nb_row, nb_column))
    for current_row in range(nb_row):
        for current_column in range(nb_column):
            matrix_tf_idf[current_row, current_column] = matrix_tf[current_row, current_column] * list_idf[
                current_column]
    return matrix_tf_idf

