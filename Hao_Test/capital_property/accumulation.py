# 作者：hao.ren3
# 时间：2019/10/14 11:41
# IDE：PyCharm

from sqlalchemy import func, MetaData
from sqlalchemy.orm import sessionmaker
from python_scraping.Hao_Test.tools.sql import create_mysql_engine
from python_scraping.Hao_Test.capital_property.Chengdu_Bank import script_chengdu_table
from datetime import timedelta
from decimal import Decimal
from pandas import DataFrame as df
if __name__ == "__main__":
    my_engine = create_mysql_engine("web_crawler")
    Session = sessionmaker(bind=my_engine)
    session = Session()
    meta_data = MetaData(my_engine)
    table = script_chengdu_table(meta_data)

    last_date_time = session.query(func.max(table.c.statistic_data)).first()[0]
    previous_day = session.query(table).filter(table.c.statistic_data==last_date_time).first()

    principal = previous_day[1]
    all_interest = previous_day[3]

    print("%f ---> %f"%(principal, all_interest))
    last_date_time = last_date_time + timedelta(days=1)

    # print("请输入一个%s得到的利息")
    daily_interest = input("请输入一个%s得到的利息" % last_date_time)
    daily_interest = Decimal(daily_interest)

    # 计算当前累计的本息总和和利息总和
    principal = principal + daily_interest
    all_interest = all_interest + daily_interest
    print("%f ---> %f"%(principal, all_interest))

    data = df({'statistic_data': [last_date_time], 'principal': [principal],
               'daily_interest': [daily_interest], 'all_interest': [all_interest]}, index=None)
    data.to_sql("chengdu_bank", con=my_engine, if_exists='append', index=None)

    my_engine.dispose()