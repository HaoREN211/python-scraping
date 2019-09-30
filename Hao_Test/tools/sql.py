# 作者：hao.ren3
# 时间：2019/9/26 11:25
# IDE：PyCharm

import MySQLdb
from sqlalchemy import create_engine

mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'hhaixdw'

def create_mysql_connection(mysql_db):
    """
    :param mysql_db:
    :return: 建立mysql链接
    """
    return MySQLdb.connect(mysql_host, mysql_user, mysql_password, mysql_db, charset='utf8')

def create_mysql_engine(mysql_db):
    string_engie = 'mysql+pymysql://'+mysql_user+':'+mysql_password+'@'+mysql_host+'/'+str(mysql_db)
    engine = create_engine(string_engie)
    return engine
