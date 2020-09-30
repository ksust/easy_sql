"""
demo: using EasyMySQLUtil to CURD operation
"""
import datetime
from sqlalchemy import Column, Integer, String, DateTime, or_
from easy_sql.easy_util import EasyMySQLUtil

# required
EasyMySQLUtil.init('../conf/conf.yml')


class Demo(EasyMySQLUtil.map_base):
    __tablename__ = 'demo'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    data = Column(String(255))
    time = Column(DateTime())


def curd_example():
    """
    EasyMySQLUtil CURD
    :return:
    """
    demo = Demo()
    demo.name = 'test'
    demo.data = '{}'
    demo.time = datetime.datetime.now()
    # create
    result = EasyMySQLUtil.add(demo)
    print('MySQLUtil create', result.__dict__)
    # retrieve
    data_list = EasyMySQLUtil.find_all(Demo, or_(Demo.name == 'ksust', Demo.id >= 40))
    print('MySQLUtil retrieve or_')
    for data in data_list:
        print(data.__dict__)
    data = EasyMySQLUtil.find_one(Demo, Demo.name == 'yg', Demo.id > 40)
    print('MySQLUtil retrieve and_ -> one')
    print(data.__dict__)
    # update
    result = EasyMySQLUtil.update(Demo, Demo.name == 'yg', time=datetime.datetime.now())
    print('MySQLUtil update', result)
    # delete
    result = EasyMySQLUtil.delete(Demo, Demo.name == 'test')
    print('MySQLUtil delete', result)


def session_example():
    # select
    cursor = EasyMySQLUtil.session.execute('select * from demo')
    result = cursor.fetchall()
    print('session_example', result)


if __name__ == '__main__':
    curd_example()
    session_example()
