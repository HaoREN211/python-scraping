# 作者：hao.ren3
# 时间：2019/10/16 18:25
# IDE：PyCharm

from python_scraping.Hao_Test.tools.sql import create_mysql_engine
from python_scraping.Hao_Test.data_base_structure.init_table import init_data_column_table, init_data_base_table, init_data_table_table
from sqlalchemy import MetaData
from sqlalchemy.orm.session import sessionmaker

if __name__ == "__main__":
    my_engine = create_mysql_engine("hao_data_base_structure")
    my_meta_data = MetaData(my_engine)
    Session = sessionmaker(bind=my_engine)
    session = Session()

    table_data_base = init_data_base_table(mysql_meta_data=my_meta_data)
    table_data_table = init_data_table_table(mysql_meta_data=my_meta_data)
    table_data_column = init_data_column_table(mysql_meta_data=my_meta_data)

    test = (table_data_column.select()
            .join(table_data_table, table_data_column.c.data_table_id==table_data_table.c.id)
            .join(table_data_base, table_data_column.c.data_base_id==table_data_base.c.id))

    test = (session.query(table_data_base.c.name, table_data_table.c.name, table_data_column.c.name)
            .join(table_data_table, table_data_column.c.data_table_id==table_data_table.c.id)
            .join(table_data_base, table_data_column.c.data_base_id == table_data_base.c.id).all())

    for current_row in test:
        print(".".join(current_row))

    my_engine.dispose()