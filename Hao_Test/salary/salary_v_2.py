# 作者：hao.ren3
# 时间：2019/10/19 15:15
# IDE：PyCharm

from python_scraping.Hao_Test.salary.salary_setting import DATA_BASE_NAME
from python_scraping.Hao_Test.tools.sql import create_mysql_engine
from sqlalchemy import Table, MetaData, Column, Date, DECIMAL, String
from python_scraping.Hao_Test.salary.list_salary import insert_list_salary

# 创建存放工资条的表
def init_salary_table(inside_meta_data):
    script_table = get_salary_table_script(inside_meta_data=inside_meta_data)
    if not script_table.exists():
        print("--->税收表格不存在，创建表格")
        script_table.create()
    return script_table

# 获取工资表格的脚本
def get_salary_table_script(inside_meta_data):
    return Table("hao_salary", inside_meta_data,
                 Column("salary_date", Date, primary_key=True, comment="工资月份"),
                 Column("employee_id", String(20), comment="员工号"),
                 Column("employee_name", String(20), comment="员工姓名"),
                 Column("enterprise_name", String(20), comment="公司名称"),
                 Column("basic_salary", DECIMAL(10, 2), comment="基本工资"),
                 Column("personal_endowment", DECIMAL(10, 2), comment="个人养老保险"),
                 Column("personal_medical", DECIMAL(10, 2), comment="个人医疗保险"),
                 Column("personal_unemployment", DECIMAL(10, 2), comment="个人失业保险保险"),
                 Column("personal_provident_fund", DECIMAL(10, 2), comment="个人公积金部分"),
                 Column("salary_before_tax", DECIMAL(10, 2), comment="税前薪资"),
                 Column("tax", DECIMAL(10, 2), comment="个人所得税"),
                 Column("salary_after_tax", DECIMAL(10, 2), comment="税后薪资"),
                 Column("enterprise_endowment", DECIMAL(10, 2), comment="公司缴纳养老保险"),
                 Column("enterprise_medical", DECIMAL(10, 2), comment="公司缴纳医疗保险"),
                 Column("enterprise_supplementary_medical", DECIMAL(10, 2), comment="公司缴纳补充医疗保险"),
                 Column("enterprise_maternity", DECIMAL(10, 2), comment="公司缴纳生育保险"),
                 Column("enterprise_occupational", DECIMAL(10, 2), comment="公司缴纳工伤保险"),
                 Column("enterprise_unemployment", DECIMAL(10, 2), comment="公司缴纳失业保险"),
                 Column("enterprise_provident_fund", DECIMAL(10, 2), comment="公司缴纳公积金"),
                 Column("enterprise_total", DECIMAL(10, 2), comment="公司缴纳总和"),
                 extend_existing=True,
                 comment="个人税收表")

if __name__ == "__main__":
    my_engine = create_mysql_engine(DATA_BASE_NAME)
    my_meta_data = MetaData(my_engine)
    insert_list_salary(init_salary_table(my_meta_data), my_engine)
    sql_update = ("UPDATE hao_salary set enterprise_total = "
                  "enterprise_endowment+enterprise_medical+enterprise_supplementary_medical+"
                  "enterprise_maternity+enterprise_occupational+enterprise_unemployment+enterprise_provident_fund")
    my_engine.execute(sql_update)
    my_engine.dispose()