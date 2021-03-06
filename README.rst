easy_sql
^^^^^^^^^^
Easy to use python sql(for kb-mysql first)

Based on SQLAlchemy

Quick Start
-----------
**Installation**: pip install easy_sql

1.config
>>>>>>>>
Edit conf/conf.yml
::

    mysql: # mysql config
      url: mysql://root:password@127.0.0.1:3306/db # mysql server
      encoding: utf-8
      pool_size: 5 # pool size
      echo: false # echo sql while executing

2.demo-mysql
>>>>>>>>>>>>>>>>>>
Table `demo`:
::

    -- ----------------------------
    -- Table structure for demo
    -- ----------------------------
    DROP TABLE IF EXISTS `demo`;
    CREATE TABLE `demo`  (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
      `data` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
      `time` datetime(0) NULL DEFAULT NULL,
      PRIMARY KEY (`id`) USING BTREE
    ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

    -- ----------------------------
    -- Records of demo
    -- ----------------------------
    INSERT INTO `demo` VALUES (1, 'ksust', '{}', '2020-09-29 15:44:57');
    INSERT INTO `demo` VALUES (2, 'ksust', '{}', '2020-09-29 15:44:57');

demo-mysql:
::

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



3.demo-mysql-util
>>>>>>>>>>>>>>>>>>>>>>>>>
::

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

