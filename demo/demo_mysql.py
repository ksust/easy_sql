"""
demo: using EasyMySQLBase
"""
import datetime
from sqlalchemy import Column, Integer, String, DateTime, or_
from easy_sql.easy_mysql_dao_base import EasyMySQLDAOBase
from easy_sql.easy_util import EasyMySQLUtil

# required
EasyMySQLUtil.init('../conf/conf.yml')


class Demo(EasyMySQLUtil.map_base):
    __tablename__ = 'demo'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    data = Column(String(255))
    time = Column(DateTime())


# Demo DAO: to operate table 'demo'
class DemoDAO(EasyMySQLDAOBase):
    def __init__(self):
        # required
        EasyMySQLDAOBase.__init__(self, Demo)


def curd_example():
    """
    EasyMySQLUtil CURD
    :return:
    """
    demo_dao = DemoDAO()
    demo = Demo()
    demo.name = 'test'
    demo.data = '{}'
    demo.time = datetime.datetime.now()
    # create
    result = demo_dao.add(demo)
    print('MySQLUtil create', result.__dict__)
    # retrieve
    data_list = demo_dao.find_all(or_(Demo.name == 'ksust', Demo.id >= 40))
    print('MySQLUtil retrieve or_')
    for data in data_list:
        print(data.__dict__)
    data = demo_dao.find_one(Demo.name == 'yg', Demo.id > 40)
    print('MySQLUtil retrieve and_ -> one')
    print(data.__dict__)
    # update
    result = demo_dao.update(Demo.name == 'yg', time=datetime.datetime.now())
    print('MySQLUtil update', result)
    # delete
    result = demo_dao.delete(Demo.name == 'test')
    print('MySQLUtil delete', result)


def session_example():
    # select
    demo_dao = DemoDAO()
    cursor = demo_dao.session.execute('select * from demo')
    result = cursor.fetchall()
    print('session_example', result)


if __name__ == '__main__':
    curd_example()
    session_example()
