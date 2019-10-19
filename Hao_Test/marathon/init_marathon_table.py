# 作者：hao.ren3
# 时间：2019/10/17 9:18
# IDE：PyCharm

from sqlalchemy import Table, Column, BigInteger, String, MetaData, Date, Boolean, Integer, and_, update
from python_scraping.Hao_Test.tools.sql import create_mysql_engine

# 获取创建马拉松的脚本
def get_table_script(function_meta_data):
    return Table("marathon", function_meta_data,
                   Column("id", BigInteger, primary_key=True, autoincrement=True, comment="主键"),
                   Column("name", String(100), nullable=False, comment="马拉松名字"),
                   Column("apply_start", Date, nullable=False, comment="报名起始日期"),
                   Column("apply_end", Date, nullable=False, comment="报名终止日期"),
                   Column("is_applied", Boolean, nullable=False, default=False, comment="是否报名比赛"),
                   Column("distance", Integer, nullable=True, comment="报名路程"),
                   Column("competition_start", Date, nullable=False, comment="比赛开始日期"),
                   Column("competition_end", Date, nullable=False, comment="比赛结束日期"),
                   Column("is_finished", Boolean, nullable=False, default=False, comment="是否完赛"),
                   comment="马拉松比赛日程", extend_existing=True)

# 创建马拉松表
def init_marathon_table(my_meta_data):
    table_script = get_table_script(my_meta_data)
    if not table_script.exists():
        table_script.create()
    return table_script


class Marathon:
    id, name, apply_start, apply_end, is_applied, distance, competition_start, competition_end, is_finished  = [None] * 9
    exist = False
    # 创建类的时候自动创建
    def __init__(self, name, apply_start, apply_end, competition_start, competition_end,
                 is_applied=False, distance=100, is_finished=False):
        self.mysql_engine = create_mysql_engine("hao_data_base_structure")
        self.meta_data = MetaData(self.mysql_engine)
        self.table_script = init_marathon_table(self.meta_data)
        self.name = name
        self.apply_start = apply_start
        self.apply_end = apply_end
        self.is_applied = is_applied
        self.distance = distance
        self.competition_start = competition_start
        self.competition_end = competition_end
        self.is_finished = is_finished
        self.insert_into_database()

    # 删除类的时候自动释放mysql句柄
    def __del__(self):
        self.mysql_engine.dispose()

    # 根据马拉松名字，报名起始日期，比赛起始日期判断该比赛是否存在于数据库
    def verify_exist(self):
        list_result = self.table_script.select(and_(
            self.table_script.c.name == self.name,
            self.table_script.c.apply_start == self.apply_start,
            self.table_script.c.apply_end == self.apply_end,
            self.table_script.c.competition_start == self.competition_start,
            self.table_script.c.competition_end == self.competition_end,
        )).execute().fetchall()
        nb_result = len(list_result)
        if nb_result > 0:
            first = list_result[0]
            self.id = first[0]
            self.exist = True
            return True
        return False

    # 将数据插入进数据库中
    def insert_into_database(self):
        if not self.verify_exist():
            print("---> 将%s的%s比赛数据插入数据库" % (self.competition_start, self.name))
            values = self.table_script.insert().values(name=self.name,
                                                       apply_start=self.apply_start,
                                                       apply_end = self.apply_end,
                                                       is_applied = self.is_applied,
                                                       distance = self.distance,
                                                       competition_start = self.competition_start,
                                                       competition_end = self.competition_end,
                                                       is_finished = self.is_finished)
            self.mysql_engine.execute(values)
            self.verify_exist()
        else:
            print("---> %s的%s比赛存在于数据库" % (self.competition_start, self.name))

    # 更新是否申请比赛的字段
    def update_is_applied(self, is_applied):
        self.is_applied = is_applied
        self.table_script.update().where(self.table_script.c.id == self.id).values(is_applied=is_applied).execute()

    # 更新跑步距离
    def update_distance(self, distance):
        self.distance = distance
        self.table_script.update().where(self.table_script.c.id == self.id).values(distance=distance).execute()

    # 更新跑步距离
    def update_is_finished(self, is_finished):
        self.is_finished = is_finished
        self.table_script.update().where(self.table_script.c.id == self.id).values(is_finished=is_finished).execute()
