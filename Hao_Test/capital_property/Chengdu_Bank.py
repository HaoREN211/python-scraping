# 作者：hao.ren3
# 时间：2019/10/14 10:55
# IDE：PyCharm
from python_scraping.Hao_Test.tools.sql import create_mysql_engine
from sqlalchemy import Table, MetaData, Column, Date, Float, DECIMAL
from pandas import DataFrame
from numpy import shape

def script_chengdu_table(inside_meta_data):
    return Table("chengdu_bank", inside_meta_data,
                  Column("statistic_data", Date, primary_key=True, comment="统计时间"),
                  Column("principal", DECIMAL(10, 2), comment="所有金额"),
                  Column("daily_interest", DECIMAL(10, 2), comment="当日利息"),
                  Column("all_interest", DECIMAL(10, 2), comment="累计利息"))

def init_chengdu_table(inside_meta_data):
    table = script_chengdu_table(inside_meta_data)
    if not table.exists():
        table.create()
    return table

def get_data():
    list_date = list(['2019-10-08', '2019-10-09', '2019-10-10', '2019-10-11', '2019-10-12'])
    list_principal = list([20000, 20002.7, 40004.03, 40007.88, 40011.98])
    list_daily_interest = list([0, 2.07, 1.96, 3.85, 4.1])
    list_all_interest = list([0, 2.07, 4.03, 7.88, 11.98])
    return DataFrame({'statistic_data': list_date, 'principal': list_principal, 'daily_interest': list_daily_interest,
                      'all_interest': list_all_interest})

if __name__ == "__main__":
    print("成都银行理财产品")
    # 初始化存放表格的数据表
    my_engine = create_mysql_engine("web_crawler")
    meta_data = MetaData(my_engine)
    table_script = init_chengdu_table(meta_data)

    # 获取当前所有的数据
    my_data = get_data()
    drop_index = list([])

    # 筛选出还未曾保存到数据库里的数据
    for current_index in range(shape(my_data)[0]):
        current_date = my_data.iloc[current_index, 0]
        result = table_script.select().where(table_script.c.statistic_data == "2019-10-08").execute().fetchall()
        nb_result = len(result)
        if nb_result>0:
            print("%s的数据已经存在，忽略" % current_date)
            drop_index.append(current_index)
    my_data.drop(index=drop_index, axis=0, inplace=True)

    # 将数据保存到数据库
    if shape(my_data)[0] > 0:
        my_data.to_sql("chengdu_bank", con=my_engine, if_exists="append", index=None)
    else:
        print("无新数据更新")
    my_engine.dispose()
