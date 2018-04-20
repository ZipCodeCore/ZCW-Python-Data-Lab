#!/usr/bin/env python
import MySQLdb as mariadb
import psycopg2 as pgsql
import yaml

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

conn = mariadb.connect(host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['password'],
        db=cfg['mysql']['db'],
        port=cfg['mysql']['port'])

with conn.cursor() as cursor:
    sql = """
        SELECT table_name FROM information_schema.tables;
    """
    cursor.execute(sql)
    result = cursor.fetchall()

conn_pg = pgsql.connect(host=cfg['pgres']['host'],
        user=cfg['pgres']['user'],
        password=cfg['pgres']['password'],
        database=cfg['pgres']['db'],
        port=cfg['pgres']['port'])

with conn_pg.cursor() as cursor_pg:
    sql = """
        SELECT table_name FROM information_schema.tables;
    """
    cursor_pg.execute(sql)
    result = cursor_pg.fetchall()
    print(result)
