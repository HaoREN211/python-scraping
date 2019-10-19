# 作者：hao.ren3
# 时间：2019/10/17 9:41
# IDE：PyCharm

from python_scraping.Hao_Test.marathon.init_marathon_table import Marathon

# 将已经报名的比赛添加进数据库中
def insert_data():
    Marathon(name="北京线上马拉松", apply_start="2019-10-11", apply_end="2019-11-02",
                        competition_start="2019-11-03", competition_end="2019-11-03", is_applied=True, distance=10)
    Marathon(name="天王星线上跑", apply_start="2019-10-08", apply_end="2019-10-23",
             competition_start="2019-10-24", competition_end="2019-10-26", is_applied=True, distance=3)
    Marathon(name="中国银行成都线上马拉松", apply_start="2019-09-30", apply_end="2019-10-26",
             competition_start="2019-10-27", competition_end="2019-10-27", is_applied=True, distance=10)
    Marathon(name="土星线上跑", apply_start="2019-09-30", apply_end="2019-10-12", is_finished=True,
             competition_start="2019-10-13", competition_end="2019-10-13", is_applied=True, distance=3)
    Marathon(name="深圳南山半程线上马拉松", apply_start="2019-09-11", apply_end="2019-11-23",
             competition_start="2019-11-24", competition_end="2019-11-24", is_applied=True, distance=5)
    Marathon(name="秦皇岛天下第一关长城国际线上马拉松", apply_start="2019-09-29", apply_end="2019-10-19",
             competition_start="2019-10-20", competition_end="2019-10-20", is_applied=True, distance=3)

if __name__ == "__main__":
    insert_data()