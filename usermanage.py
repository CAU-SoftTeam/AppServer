import os
import pymysql
from databaseManage import Database

def register():
    conn = Database.get_connection()
    curs = conn.cursor()
    sql = """INSERT INTO `userdata`.`user` (`id`, `name`) VALUES ('3', 'jang');"""
    curs.execute(sql)
    conn.commit()
    conn.close()