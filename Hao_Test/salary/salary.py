# 作者：hao.ren3
# 时间：2019/10/11 9:47
# IDE：PyCharm
from numpy import shape
from pandas import read_excel
from python_scraping.Hao_Test.func.date import is_date_string
from python_scraping.Hao_Test.tools.sql import create_mysql_engine
from sqlalchemy import Table, MetaData, Column, Date, String, Float


def init_salary_table(inside_my_engine):
    """
    :return: 初始化并创建薪资表
    """
    meta_data = MetaData(inside_my_engine)
    table = get_salary_script(meta_data)
    if not table.exists():
        print("正在创建薪资表")
        table.create()

def get_salary_script(inside_meta_data):
    """
    :return: 返回薪资表的描述
    """
    return Table("salary", inside_meta_data,
                  Column("salary_date", Date, primary_key=True, comment="主键"),
                  Column("employee_id", String(20), comment="工号"),
                  Column("employee_name", String(20), comment="员工姓名"),
                  Column("basic_salary", Float, comment="应发工资"),
                  Column("pension", Float, comment="个人养老部分"),
                  Column("medical", Float, comment="个人医疗部分"),
                  Column("unemployment_insurance", Float, comment="个人失业保险金部分"),
                  Column("provident_fund", Float, comment="个人公积金"),
                  Column("salary_before_tax", Float, comment="税前薪资"),
                  Column("tax", Float, comment="个人所得税"),
                  Column("salary_after_tax", Float, comment="税后薪资"))

if __name__ == "__main__":
    my_engine = create_mysql_engine("web_crawler")
    meta_data = MetaData(my_engine)
    table = get_salary_script(meta_data)

    # 创建存放薪资数据的表
    init_salary_table(my_engine)

    # 存放薪资数据的文件位置
    file_name = r'C:\Users\hao.ren3\Desktop\HCB.xlsx'
    data = read_excel(file_name, header=0, sheet_name=1)

    # 选取目标特征
    sub_date = data.iloc[[0, 1], [0, 1, 2, 16, 17, 18, 19, 23, 26, 27, 32]]
    sub_date.columns = ["salary_date", "employee_id", "employee_name",
                        "basic_salary", "pension", "medical", "unemployment_insurance",
                        "provident_fund", "salary_before_tax", "tax",
                        "salary_after_tax"]
    nb_row, nb_column = shape(sub_date)
    drop_row = list([])

    # 将日期格式正确的未存入数据库的薪资明细筛选出来
    for current_row in range(nb_row):
        salary_date = is_date_string(str(sub_date.iloc[current_row, 0]))
        if not salary_date is None:
            nb = len(table.select(table.c.salary_date == salary_date).execute().fetchall())
            if nb > 0:
                drop_row.append(current_row)
                print("--->%s当月薪资条已经存在，不需要插入数据" % salary_date)
            else:
                print("--->%s插入数据" % salary_date)
        else:
            print("--->%s当月日期格式存在问题，不需要插入数据" % salary_date)
            drop_row.append(current_row)
    if len(drop_row)>0:
        sub_date.drop(index=drop_row, axis=0, inplace=True)

    # 存入数据库
    sub_date.to_sql('salary', con=my_engine, if_exists="append", index=False)
    my_engine.dispose()