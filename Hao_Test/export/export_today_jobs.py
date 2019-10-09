# 作者：hao.ren3
# 时间：2019/10/8 16:40
# IDE：PyCharm

if __name__ == "__main__":
    from time import localtime, strftime
    from python_scraping.Hao_Test.tools.sql import create_mysql_engine
    from python_scraping.Hao_Test.tools.scrapt_web import get_liepin_table_script
    from sqlalchemy.orm import sessionmaker
    from pandas import DataFrame as DF

    my_engine = create_mysql_engine("web_crawler")
    Session = sessionmaker(bind=my_engine)
    session = Session()

    current_date = strftime("%Y-%m-%d", localtime())
    file_name = r'C:\Users\hao.ren3\Desktop\liepin_'+current_date+'.xlsx'
    jobs_table = get_liepin_table_script(my_engine)

    result = jobs_table.select(jobs_table.c.execute_time.like(current_date+"%")).execute().fetchall()
    title = list([])
    company = list([])
    salary_min = list([])
    salary_max = list([])
    salary_unit = list([])
    city = list([])
    district = list([])
    degree = list([])
    experience = list([])
    language = list([])
    age = list([])
    link = list([])
    for current_individual in result:
        title.append(current_individual[1])
        company.append(current_individual[3])
        salary_min.append(current_individual[4])
        salary_max.append(current_individual[5])
        salary_unit.append(current_individual[6])
        city.append(current_individual[7])
        district.append(current_individual[8])
        degree.append(current_individual[9])
        experience.append(current_individual[10])
        language.append(current_individual[11])
        age.append(current_individual[12])
        link.append(current_individual[13])
    data = DF({'title': title, 'company': company, 'salary_min': salary_min, 'salary_max': salary_max,
               'salary_unit': salary_unit, 'city': city, 'district': district, 'degree': degree, 'experience': experience,
               'language': language, 'age': age, 'link': link})
    data['salary_min'] = data['salary_min'].apply(lambda x: 0 if x=='' else int(x)).copy()
    data = data.sort_values(by=['salary_min'], ascending=False)
    data.to_excel(file_name, index=None, encoding='utf_8_sig')

    session.close()
    my_engine.dispose()
