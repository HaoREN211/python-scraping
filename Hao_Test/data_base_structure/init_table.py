# 作者：hao.ren3
# 时间：2019/10/16 11:40
# IDE：PyCharm

TABLE_NAME_DATA_BASE = "data_base"
TABLE_NAME_DATA_TABLE = "data_table"
TABLE_NAME_DATA_COLUMN = "data_column"

from python_scraping.Hao_Test.tools.sql import create_mysql_engine
from sqlalchemy import MetaData, Table, BigInteger, String, Column, Text, ForeignKey, Integer, UniqueConstraint, \
    TIMESTAMP, and_
from pandas import read_excel
from time import strftime, localtime

# 创建hao_data_base_structure数据库
def create_data_base_engine():
    inside_my_engine = create_mysql_engine("mysql")
    sql = "create database IF NOT EXISTS hao_data_base_structure DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci"
    inside_my_engine.execute(sql)
    inside_my_engine.dispose()
    return create_mysql_engine("hao_data_base_structure")

# 创建存放数据库信息的data_base数据表
def init_data_base_table(mysql_meta_data):
    data_base_table = Table(TABLE_NAME_DATA_BASE, mysql_meta_data,
                            Column("id", BigInteger, primary_key=True, autoincrement=True, comment="主键"),
                            Column("name", String(100), comment="数据库名字", unique=True),
                            Column("description", Text, comment="描述"),
                            Column("create_time", TIMESTAMP, comment="创建时间"),
                            extend_existing=True)
    if not data_base_table.exists():
        print("创建%s表格" % TABLE_NAME_DATA_BASE)
        data_base_table.create()
    return data_base_table

# 创建存放数据表信息的data_table数据表
def init_data_table_table(mysql_meta_data):
    data_base = init_data_base_table(mysql_meta_data=mysql_meta_data)
    data_table_table = Table(TABLE_NAME_DATA_TABLE, mysql_meta_data,
                            Column("id", BigInteger, primary_key=True, autoincrement=True, comment="主键"),
                            Column("data_base_id", BigInteger, ForeignKey(data_base.c.id), comment="数据库data_base.id"),
                            Column("name", String(100), comment="数据表名字"),
                            Column("description", Text, comment="描述"),
                            Column("create_time", TIMESTAMP, comment="创建时间"),
                            UniqueConstraint("data_base_id", "name"),
                            extend_existing=True)
    if not data_table_table.exists():
        print("创建%s表格" % TABLE_NAME_DATA_TABLE)
        data_table_table.create()
    return data_table_table

# 创建存放字段信息的data_column数据表
def init_data_column_table(mysql_meta_data):
    data_base = init_data_base_table(mysql_meta_data=mysql_meta_data)
    data_table = init_data_table_table(mysql_meta_data=mysql_meta_data)
    data_column_table = Table(TABLE_NAME_DATA_COLUMN, mysql_meta_data,
                            Column("id", BigInteger, primary_key=True, autoincrement=True, comment="主键"),
                            Column("data_base_id", BigInteger, ForeignKey(data_base.c.id), comment="数据库data_base.id"),
                            Column("data_table_id", BigInteger, ForeignKey(data_table.c.id), comment="数据表data_table.id"),
                            Column("name", String(100), comment="字段名字"),
                            Column("description", Text, comment="描述"),
                            Column("position", Integer, comment="字段在数据表中的位置"),
                            Column("create_time", TIMESTAMP, comment="创建时间"),
                            UniqueConstraint("data_base_id", "data_table_id", "name"),
                            UniqueConstraint("data_table_id", "position"),
                            extend_existing=True)
    if not data_column_table.exists():
        print("创建%s表格" % TABLE_NAME_DATA_COLUMN)
        data_column_table.create()
    return data_column_table

# 删掉表中所有的表
def delete_all_table(mysql_meta_data):
    inside_table_data_base = init_data_base_table(mysql_meta_data=mysql_meta_data)
    inside_table_data_table = init_data_table_table(mysql_meta_data=mysql_meta_data)
    inside_table_data_column = init_data_column_table(mysql_meta_data=mysql_meta_data)
    list_table = list([inside_table_data_column, inside_table_data_table, inside_table_data_base])
    for current_table in list_table:
        if current_table.exists():
            current_table.drop()

# 获取当前时间字符串格式，包含年月日，时分秒
def get_current_timestamp_string():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

# 根据数据库的名字找回数据库的id
def find_data_base_id_by_name(database_name):
    # 判断数据是否存在，存在的话返回id，否则先创建数据再返回id
    list_database = table_data_base.select(table_data_base.c.id).where(
        table_data_base.c.name == database_name).execute().fetchall()
    nb_database = len(list_database)
    if nb_database == 0:
        insert_script = table_data_base.insert()
        execute_time = get_current_timestamp_string()
        insert_script = insert_script.values(name=database_name, create_time=execute_time)
        my_engine.execute(insert_script)
    list_database = table_data_base.select(table_data_base.c.id).where(
        table_data_base.c.name == database_name).execute().first()
    data_base_id = int(list_database[0])
    return data_base_id

# 根据数据库名字和数据表名字找回存放数据库信息和数据表信息的id
def find_table_id_by_name(database_name, table_name):
    database_id = find_data_base_id_by_name(database_name)
    list_table = (table_data_table.select(table_data_table.c.id)
                  .where(and_(table_data_table.c.name==table_name, table_data_table.c.data_base_id==database_id))
                  .execute()
                  .fetchall())
    nb_table = len(list_table)
    if nb_table == 0:
        insert_script = table_data_table.insert()
        execute_time = get_current_timestamp_string()
        insert_script = insert_script.values(data_base_id=database_id, name=table_name, create_time=execute_time)
        my_engine.execute(insert_script)
    table_table = (table_data_table.select(table_data_table.c.id)
                   .where(and_(table_data_table.c.name == table_name, table_data_table.c.data_base_id == database_id))
                   .execute()
                   .first())
    table_id = table_table[0]
    return database_id, table_id

# 判断数据库名、表名、字段名是否存在
def verify_column_name_exist(database_name, table_name, column_name):
    database_id, table_id = find_table_id_by_name(database_name, table_name)
    list_column_name = (table_data_column.select()
        .where(and_(table_data_column.c.data_base_id==database_id,
                    table_data_column.c.data_table_id==table_id,
                    table_data_column.c.name==column_name)
               ).execute().fetchall())
    if len(list_column_name) == 0:
        return False
    else:
        return True

# 将数据库中不存在的数据存入数据库
def insert_into_database(list_data_base_name, list_data_table_name, list_data_column_name, list_data_position, list_data_description):
    if len(list_data_base_name) != len(list_data_table_name):
        return False
    if len(list_data_base_name) != len(list_data_column_name):
        return False
    if len(list_data_base_name) != len(list_data_position):
        return False
    if len(list_data_base_name) != len(list_data_description):
        return False
    list_to_insert = list([])
    for i in range(len(list_data_base_name)):
        current_data_base = str(list_data_base_name[i]).strip()
        current_data_table = str(list_data_table_name[i]).strip()
        current_data_column = str(list_data_column_name[i]).strip()
        current_data_position = int(list_data_position[i])
        current_data_description = str(list_data_description[i]).strip()
        if not verify_column_name_exist(current_data_base, current_data_table, current_data_column):
            print("--->插入中%s.%s.%s" % (current_data_base, current_data_table, current_data_column))
            current_data_base_id, current_data_table_id = find_table_id_by_name(current_data_base, current_data_table)
            execute_time = get_current_timestamp_string()
            list_to_insert.append({"data_base_id": current_data_base_id,
                                   "data_table_id": current_data_table_id,
                                   "name": current_data_column,
                                   "description": current_data_description,
                                   "position": current_data_position,
                                   "create_time": execute_time})
        else:
            print("--->已存在%s.%s.%s" % (current_data_base, current_data_table, current_data_column))
    if len(list_to_insert) > 0:
        my_engine.execute(table_data_column.insert(), list_to_insert)
    return True

# 插入白条司机贷款字段数据
def insert_user_bt_cash_ovd_info():
    file_path = r'C:\Users\hao.ren3\Desktop\逾期表字段汇总.xlsx'
    data = read_excel(file_path, header=0)
    insert_into_database(data.database.values, data.table.values, data.name.values, data.position.values, data.description.values)

# 插入各业务先贷款字段数据
def insert_user_loan_ovd_base_info():
    file_path = r'C:\Users\hao.ren3\Desktop\逾期表字段汇总.xlsx'
    data = read_excel(file_path, header=0, sheet_name=1)
    insert_into_data_base(data)

def insert_umd_user_base_info_s_d():
    file_path = r'C:\Users\hao.ren3\Desktop\文档\数据\umd_user_base_info_s_d.xlsx'
    data = read_excel(file_path, header=0)
    insert_into_data_base(data)

def insert_into_data_base(inside_data):
    insert_into_database(inside_data.database.values,
                         inside_data.table.values,
                         inside_data.name.values,
                         inside_data.position.values,
                         inside_data.description.values)


if __name__ == "__main__":
    my_engine = create_data_base_engine()
    my_meta_data = MetaData(my_engine)
    table_data_base = init_data_base_table(mysql_meta_data=my_meta_data)
    table_data_table = init_data_table_table(mysql_meta_data=my_meta_data)
    table_data_column = init_data_column_table(mysql_meta_data=my_meta_data)
    insert_umd_user_base_info_s_d()
    # insert_user_loan_ovd_base_info()
    my_engine.dispose()