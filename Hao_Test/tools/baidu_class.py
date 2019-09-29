# 作者：hao.ren3
# 时间：2019/9/26 11:46
# IDE：PyCharm

import string
from urllib.parse import quote

from tools.scrapt_web import get_web_content
from tools.scrapt_web import get_web_content_item
from tools.sql import create_mysql_connection


class baidu_person:
    mysql_db = 'baidu'
    baidu_item = 'https://baike.baidu.com/item/'
    web_content = ''

    object_link = ''
    object_person_name = ''
    object_foreign_name = ''
    object_nationality = ''
    object_family = ''
    object_constellation = ''
    object_blood_group = ''
    object_height = ''
    object_birth_place = ''
    object_birth_day = ''
    object_profession = ''
    object_school = ''
    object_agency = ''
    object_gender = ''
    object_experience = ''
    object_weight = ''
    object_spouse = ''
    object_chinese_birth_day = ''

    def __init__(self):
        """
        创建数据库链接
        """
        print("创建数据库连接")
        self.create_database()
        self.db_connection = create_mysql_connection(mysql_db=self.mysql_db)
        self.db_cursor = self.db_connection.cursor()
        self.create_baidu_table()

    def create_baidu_table(self):
        """
        :return:创建存放人物信息的表
        """
        print("---> 创建person表")
        sql = """CREATE TABLE IF NOT EXISTS person(
        id INT PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
        chinese_name VARCHAR(100) COMMENT '中文名',
        foreign_name VARCHAR(100) COMMENT '英文名',
        nationality VARCHAR(100) COMMENT '国籍',
        family VARCHAR(100) COMMENT '民族',
        constellation VARCHAR(100) COMMENT '星座',
        blood_group VARCHAR(100) COMMENT '血型',
        height VARCHAR(100) COMMENT '身高',
        weight VARCHAR(100) COMMENT '体重',
        spouse VARCHAR(100) COMMENT '配偶',
        birth_place VARCHAR(100) COMMENT '出生地',
        birth_day VARCHAR(100) COMMENT '出生年月',
        chinese_birth_day VARCHAR(100) COMMENT '农历生日',
        profession VARCHAR(100) COMMENT '职业',
        school VARCHAR(100) COMMENT '毕业院校',
        agency VARCHAR(100) COMMENT '经纪公司',
        gender VARCHAR(100) COMMENT '性别',
        experience TEXT COMMENT '主要经历', 
        link VARCHAR(1000) COMMENT '链接')"""
        self.db_cursor.execute(sql)

    def __del__(self):
        """
        :return: 关闭数据库链接
        """
        print("销毁数据库连接")
        self.db_cursor.close()
        self.db_connection.close()

    def get_person_web(self, name):
        """
        :param name:
        :return: 给定人物名字，返回百度词条里关于该人物的信息
        """
        self.clear_attribut()
        current_page = self.baidu_item + str(name)
        self.object_link = quote(current_page, safe=string.printable)
        if not self.if_current_person_in_db():
            web_content = self.web_content = get_web_content(current_page)
            self.object_person_name = get_web_content_item(web_content, 'h1', {})
            self.get_personal_basic_info()
            self.object_experience = "".join(get_web_content_item(web_content, 'div',
                                                          {"class": "para", "label-module": "para"},
                                                          is_text=True, get_all=True))
            self.object_experience = str(self.object_experience).replace("。", "。\n")
            self.store_into_mysql()
        # self.print_basic_info()

    def create_database(self):
        """
        :return: 创建存放百度人物数据的数据库
        """
        print("---> 创建%s数据库" % self.mysql_db)
        connection = create_mysql_connection(mysql_db="mysql")
        cursor = connection.cursor()
        cursor.execute("create database IF NOT EXISTS " + self.mysql_db + " DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
        cursor.close()
        connection.close()

    def get_personal_basic_info(self):
        """
        :return:从类为basic-info cmn-clearfix的专栏里获取人物的基本信息
        """
        list_basic_info = get_web_content_item(self.web_content, 'div',
                                               {'class': 'basic-info cmn-clearfix'},
                                               is_text=False)
        dl_list = get_web_content_item(list_basic_info, 'dt',
                                       {'class': 'basicInfo-item name'}, get_all=True)
        dd_list = get_web_content_item(list_basic_info, 'dd',
                                       {'class': 'basicInfo-item value'}, get_all=True)
        for current_index in range(len(dl_list)):
            current_dl = dl_list[current_index]
            current_dd = dd_list[current_index]
            if current_dl == '中文名':
                pass
            elif current_dl == '外文名':
                self.object_foreign_name = current_dd
            elif current_dl == '国籍':
                self.object_nationality = current_dd
            elif current_dl == '民族':
                self.object_family = current_dd
            elif current_dl == '星座':
                self.object_constellation = current_dd
            elif current_dl == '血型':
                self.object_blood_group = current_dd
            elif current_dl == '身高':
                self.object_height = current_dd
            elif current_dl == '出生地':
                self.object_birth_place = current_dd
            elif current_dl == '出生日期':
                self.object_birth_day = current_dd
            elif current_dl == '职业':
                self.object_profession = current_dd
            elif current_dl == '毕业院校':
                self.object_school = current_dd
            elif current_dl == '经纪公司':
                self.object_agency = current_dd
            elif current_dl == '性别':
                self.object_gender = current_dd
            elif current_dl == '代表作品':
                pass
            elif current_dl == '主要成就':
                pass
            elif current_dl == '体重':
                self.object_weight = current_dd
            elif current_dl == '配偶':
                self.object_spouse = current_dd
            elif current_dl == '农历生日':
                self.object_chinese_birth_day = current_dd
            else:
                print("!!! not find dl %s" % current_dl)

    def print_basic_info(self):
        print(self.object_person_name)
        print(self.object_gender)
        print(self.object_foreign_name)
        print(self.object_nationality)
        print(self.object_family)
        print(self.object_constellation)
        print(self.object_blood_group)
        print(self.object_height)
        print(self.object_birth_day)
        print(self.object_birth_place)
        print(self.object_profession)
        print(self.object_school)
        print(self.object_agency)
        print(self.object_experience)
        print(self.object_link)

    def store_into_mysql(self):
        print("---> 将%s的个人信息写入数据库" % self.object_person_name)
        sql = """
        INSERT INTO `person`(`chinese_name`, `foreign_name`, `nationality`, `family`, `constellation`, 
        `blood_group`, `height`, `birth_place`, `birth_day`, `profession`, `school`, `agency`, `gender`, 
        `experience`, `link`, `weight`, `spouse`, `chinese_birth_day`) VALUES ('"""+self.object_person_name+"""','"""+self.object_foreign_name+"""',
        '"""+self.object_nationality+"""','"""+self.object_family+"""','"""+self.object_constellation+"""',
        '"""+self.object_blood_group+"""','"""+self.object_height+"""','"""+self.object_birth_place+"""',
        '"""+self.object_birth_day+"""','"""+self.object_profession+"""','"""+self.object_school+"""',
        '"""+self.object_agency+"""','"""+self.object_gender+"""','"""+self.object_experience+"""',
        '"""+self.object_link+"""', '"""+self.object_weight+"""', '"""+self.object_spouse+"""'
        , '"""+self.object_chinese_birth_day+"""')"""
        self.db_cursor.execute(sql)
        self.db_connection.commit()

    def if_current_person_in_db(self):
        sql = "select * from person WHERE link='" + str(self.object_link) + "'"
        self.db_cursor.execute(sql)
        nb_record = len(self.db_cursor.fetchall())
        if nb_record == 0:
            return False
        else:
            return True

    def clear_attribut(self):
        self.object_link = ''
        self.object_person_name = ''
        self.object_foreign_name = ''
        self.object_nationality = ''
        self.object_family = ''
        self.object_constellation = ''
        self.object_blood_group = ''
        self.object_height = ''
        self.object_birth_place = ''
        self.object_birth_day = ''
        self.object_profession = ''
        self.object_school = ''
        self.object_agency = ''
        self.object_gender = ''
        self.object_experience = ''
        self.object_weight = ''
        self.object_spouse = ''
        self.object_chinese_birth_day = ''