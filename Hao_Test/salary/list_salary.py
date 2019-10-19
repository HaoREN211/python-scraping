# 作者：hao.ren3
# 时间：2019/10/19 15:39
# IDE：PyCharm
def verify_exist(script_table, salary_date):
    """
    :param script_table:
    :param salary_date:
    :return:
    """
    list_result = (script_table.select()
                   .where(script_table.c.salary_date==salary_date)
                   .execute().fetchall())
    nb_result = len(list_result)
    if nb_result > 0:
        return True
    return False

def insert_list_salary(script_table, my_engine):
    insert_2018_07(script_table, my_engine)
    insert_2018_08(script_table, my_engine)
    insert_2018_09(script_table, my_engine)
    insert_2018_10(script_table, my_engine)
    insert_2018_11(script_table, my_engine)
    insert_2018_12(script_table, my_engine)
    insert_2019_01(script_table, my_engine)
    insert_2019_02(script_table, my_engine)
    insert_2019_03(script_table, my_engine)
    insert_2019_04(script_table, my_engine)
    insert_2019_05(script_table, my_engine)
    insert_2019_06(script_table, my_engine)
    insert_2019_07(script_table, my_engine)
    insert_2019_08(script_table, my_engine)
    insert_2019_09(script_table, my_engine)

def insert_2018_07(script_table, my_engine):
    current_date = "2018_07_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 12000,
            personal_endowment = 960,
            personal_medical = 0,
            personal_unemployment = 0,
            personal_provident_fund = 0,
            salary_before_tax = 11840,
            tax = 0,
            salary_after_tax = 6980.82,
            enterprise_endowment = 2280,
            enterprise_medical = 0,
            enterprise_supplementary_medical = 0,
            enterprise_maternity = 0,
            enterprise_occupational = 0,
            enterprise_unemployment = 0,
            enterprise_provident_fund = 0,
            enterprise_total = 0
        )
        # print(execute_script)
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2018_08(script_table, my_engine):
    current_date = "2018_08_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 12000,
            personal_endowment = 960,
            personal_medical = 240,
            personal_unemployment = 48,
            personal_provident_fund = 1440,
            salary_before_tax = 9312,
            tax = 0,
            salary_after_tax = 9383,
            enterprise_endowment = 2280,
            enterprise_medical = 780,
            enterprise_supplementary_medical = 120,
            enterprise_maternity = 96,
            enterprise_occupational = 29.4,
            enterprise_unemployment = 72,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        # print(execute_script)
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2018_09(script_table, my_engine):
    current_date = "2018_09_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 12000,
            personal_endowment = 791.28,
            personal_medical = 197.82,
            personal_unemployment = 39.56,
            personal_provident_fund = 1440,
            salary_before_tax = 9891,
            tax = 339.28,
            salary_after_tax = 9551.72,
            enterprise_endowment = 1879.29,
            enterprise_medical = 642.92,
            enterprise_supplementary_medical = 98.91,
            enterprise_maternity = 79.13,
            enterprise_occupational = 24.23,
            enterprise_unemployment = 59.35,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2018_10(script_table, my_engine):
    current_date = "2018_10_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 12800,
            personal_endowment = 1024,
            personal_medical = 256,
            personal_unemployment = 51.2,
            personal_provident_fund = 1440,
            salary_before_tax = 10028.8,
            tax = 246.8,
            salary_after_tax = 9782,
            enterprise_endowment = 2432,
            enterprise_medical = 832,
            enterprise_supplementary_medical = 128,
            enterprise_maternity = 102.4,
            enterprise_occupational = 31.36,
            enterprise_unemployment = 76.8,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2018_11(script_table, my_engine):
    current_date = "2018_11_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 12800,
            personal_endowment = 1024,
            personal_medical = 256,
            personal_unemployment = 51.2,
            personal_provident_fund = 1440,
            salary_before_tax = 10028.8,
            tax = 246.8,
            salary_after_tax = 9782,
            enterprise_endowment = 2432,
            enterprise_medical = 832,
            enterprise_supplementary_medical = 128,
            enterprise_maternity = 102.4,
            enterprise_occupational = 31.36,
            enterprise_unemployment = 76.8,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2018_12(script_table, my_engine):
    current_date = "2018_12_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 12800,
            personal_endowment = 1024,
            personal_medical = 256,
            personal_unemployment = 51.2,
            personal_provident_fund = 1440,
            salary_before_tax = 10028.8,
            tax = 246.8,
            salary_after_tax = 9782,
            enterprise_endowment = 2432,
            enterprise_medical = 832,
            enterprise_supplementary_medical = 128,
            enterprise_maternity = 102.4,
            enterprise_occupational = 31.36,
            enterprise_unemployment = 76.8,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_01(script_table, my_engine):
    current_date = "2019_01_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 12800,
            personal_endowment = 1024,
            personal_medical = 256,
            personal_unemployment = 51.2,
            personal_provident_fund = 1440,
            salary_before_tax = 10028.8,
            tax = 246.8,
            salary_after_tax = 10179.8,
            enterprise_endowment = 2432,
            enterprise_medical = 832,
            enterprise_supplementary_medical = 128,
            enterprise_maternity = 102.4,
            enterprise_occupational = 31.36,
            enterprise_unemployment = 76.8,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_02(script_table, my_engine):
    current_date = "2019_02_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 12800,
            personal_endowment = 1024,
            personal_medical = 256,
            personal_unemployment = 51.2,
            personal_provident_fund = 1440,
            salary_before_tax = 0,
            tax = 0,
            salary_after_tax = 11565.39,
            enterprise_endowment = 2432,
            enterprise_medical = 832,
            enterprise_supplementary_medical = 128,
            enterprise_maternity = 102.4,
            enterprise_occupational = 31.36,
            enterprise_unemployment = 76.8,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_03(script_table, my_engine):
    current_date = "2019_03_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 13060,
            personal_endowment = 1044.8,
            personal_medical = 261.2,
            personal_unemployment = 52.24,
            personal_provident_fund = 1440,
            salary_before_tax = 0,
            tax = 0,
            salary_after_tax = 11792.13,
            enterprise_endowment = 2481.4,
            enterprise_medical = 848.9,
            enterprise_supplementary_medical = 130.6,
            enterprise_maternity = 104.48,
            enterprise_occupational = 32,
            enterprise_unemployment = 78.36,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_04(script_table, my_engine):
    current_date = "2019_04_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 14488,
            personal_endowment = 1159.04,
            personal_medical = 289.76,
            personal_unemployment = 57.95,
            personal_provident_fund = 1440,
            salary_before_tax = 0,
            tax = 0,
            salary_after_tax = 12557.43,
            enterprise_endowment = 2752.72,
            enterprise_medical = 941.72,
            enterprise_supplementary_medical = 144.88,
            enterprise_maternity = 115.9,
            enterprise_occupational = 56.79,
            enterprise_unemployment = 86.93,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_05(script_table, my_engine):
    current_date = "2019_05_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 14668,
            personal_endowment = 1173.44,
            personal_medical = 293.36,
            personal_unemployment = 58.67,
            personal_provident_fund = 1440,
            salary_before_tax = 0,
            tax = 0,
            salary_after_tax = 29814.06,
            enterprise_endowment = 2346.88,
            enterprise_medical = 953.42,
            enterprise_supplementary_medical = 146.68,
            enterprise_maternity = 117.34,
            enterprise_occupational = 41.07,
            enterprise_unemployment = 88.01,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_06(script_table, my_engine):
    current_date = "2019_06_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 15835,
            personal_endowment = 1266.8,
            personal_medical = 316.7,
            personal_unemployment = 63.34,
            personal_provident_fund = 1440,
            salary_before_tax = 0,
            tax = 0,
            salary_after_tax = 16519.01,
            enterprise_endowment = 2533.6,
            enterprise_medical = 1029.28,
            enterprise_supplementary_medical = 158.35,
            enterprise_maternity = 126.68,
            enterprise_occupational = 44.34,
            enterprise_unemployment = 95.01,
            enterprise_provident_fund = 1440,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_07(script_table, my_engine):
    current_date = "2019_07_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 16179,
            personal_endowment = 1294.32,
            personal_medical = 323.58,
            personal_unemployment = 64.72,
            personal_provident_fund = 1527,
            salary_before_tax = 0,
            tax = 0,
            salary_after_tax = 14594,
            enterprise_endowment = 2588.64,
            enterprise_medical = 1051.64,
            enterprise_supplementary_medical = 161.79,
            enterprise_maternity = 129.43,
            enterprise_occupational = 45.3,
            enterprise_unemployment = 97.07,
            enterprise_provident_fund = 1527,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_08(script_table, my_engine):
    current_date = "2019_08_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "rwx592490 61789",
            employee_name = "任皓",
            enterprise_name = "鼎桥通讯技术有限公司",
            basic_salary = 16179,
            personal_endowment = 1294.32,
            personal_medical = 323.58,
            personal_unemployment = 64.72,
            personal_provident_fund = 1527,
            salary_before_tax = 0,
            tax = 0,
            salary_after_tax = 14275.43,
            enterprise_endowment = 2588.64,
            enterprise_medical = 1051.64,
            enterprise_supplementary_medical = 161.79,
            enterprise_maternity = 129.43,
            enterprise_occupational = 45.3,
            enterprise_unemployment = 97.07,
            enterprise_provident_fund = 1527,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)

def insert_2019_09(script_table, my_engine):
    current_date = "2019_09_01"
    if not verify_exist(script_table, current_date):
        execute_script = script_table.insert().values(
            salary_date = current_date,
            employee_id = "A1017306",
            employee_name = "任皓",
            enterprise_name = "成都运力技术有限公司",
            basic_salary = 18000,
            personal_endowment = 1294.32,
            personal_medical = 323.58,
            personal_unemployment = 64.72,
            personal_provident_fund = 1080,
            salary_before_tax = 15237.4,
            tax = 307.12,
            salary_after_tax = 14930.26,
            enterprise_endowment = 2588.64,
            enterprise_medical = 1051.64,
            enterprise_supplementary_medical = 161.79,
            enterprise_maternity = 129.43,
            enterprise_occupational = 16.18,
            enterprise_unemployment = 97.07,
            enterprise_provident_fund = 1080,
            enterprise_total = 0
        )
        print("--->正在插入%s月的工资条" % current_date)
        my_engine.execute(execute_script)
    else:
        print("--->%s月的工资条已经存在" % current_date)
