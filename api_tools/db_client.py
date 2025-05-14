from utils.logger import get_logger
import pymysql
from dbutils.pooled_db import PooledDB
from typing import Union, List

logger = get_logger()
TESTHUB_DB = {'host': '192.168.1.26',
              "port": 3306,
              'user': 'platform_db',
              'password': 'Tqs2nHFn4pvg',
              'charset': 'utf8',
              # 'echo':False,
              # 'pool_size':10,
              # 'max_overflow':20
              }

OTD_DB = {'host': 'onedb-boss-qa.weizhipin.com',  # 陆港融合一般都在boss_victoria库里
          "port": 3316,
          'user': 'j__pro_drlv',
          'password': 'RFn7QrkcBX8tFD0gah',
          'charset': 'utf8'}

REDIS_ZPHUNTER = {
    'host': '192.168.26.175',
    'port': 6479,
    'password': 'yCVnjyC5YRhA',
    'decode_responses': True
}


class MySqlDB:
    def __init__(self, db_name='platform_db', field=True, DB=None):
        '''
        创建连接
        :param db_name: 数据库名称，可缺省
        :param field: 查询返回结果是否需要带上字段名。 例：True时 ({'id':1,'name':'xxx'},{})；Fasle时((1,'xxx'),())
        :param DB: 数据库信息，缺省默认连接 testhub的数据库
        '''

        self.DB = DB if DB else TESTHUB_DB
        self.db_name = db_name
        self.field = field
        cursor = pymysql.cursors.DictCursor if self.field else pymysql.cursors.Cursor
        self.pool = PooledDB(
            creator=pymysql,  # 指定使用的数据库模块
            database=db_name,  # 数据库名称
            cursorclass=cursor,
            **self.DB
        )

    def __enter__(self):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql: str, values: tuple=None):
        with self:
            try:
                self.cursor.execute(sql, values)
                self.conn.commit()
            except Exception as e:
                logger.error(f'数据操作失败:{sql + "::" + str(values)}\n操作结果:{e}')
                self.conn.rollback()

    def query(self, sql: str, values: tuple = None, all_result=False) -> Union[dict, List[dict]]:
        """

        :param sql:
        :param values:
        :param all_result: True-返回所有查询结果；False-返回第一条结果
        :return:
        """
        logger.debug(sql + '::' + str(values))
        with self:
            self.cursor.execute(sql, values)
            if all_result:
                result = self.cursor.fetchall()
            else:
                result = self.cursor.fetchone()
            logger.debug(result)
            return result


testhub_db = MySqlDB(db_name='platform_db', DB=TESTHUB_DB)
otd_db = MySqlDB(db_name='boss_victoria', DB=OTD_DB)

if __name__ == '__main__':
    sql = 'select * from boss_tools_cookie_config where account=%s and system_name=%s'
    data=("zhongfanglu@kanzhun.com",'admin')
    res = testhub_db.query(sql=sql, values=("zhongfanglu@kanzhun.com", "admin"), all_result=True)

    # sql2='insert into hunter_ui_auto_record (case_name,type,status) values (%s,%s,%s)'
    # update_sql = 'update boss_tools_cookie_config set cookie=%s where notice_email=%s'
    # input_data = ("t_boss_newadmin=2es1lcvqhGZNLF7dKT5iNi","zhongfanglu@kanzhun.com")
    # res = testhub_db.execute(update_sql,values=input_data)

    print(res)
