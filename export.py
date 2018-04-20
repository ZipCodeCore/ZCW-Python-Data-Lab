#!/usr/bin/env python
import MySQLdb as mariadb
import psycopg2 as pgsql
import yaml
import csv

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

conn = mariadb.connect(host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['password'],
        db=cfg['mysql']['db'],
        port=cfg['mysql']['port'])

leads = []

with conn.cursor() as cursor:
    sql = """
        SELECT * FROM proleads;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        leads.append({
            'first_name': r[1],
            'last_name': r[2],
            'email': r[3],
            'gender': r[4],
            'tags': r[5],
            'phone': None,
            'employer': None
        })


conn_pg = pgsql.connect(host=cfg['pgres']['host'],
        user=cfg['pgres']['user'],
        password=cfg['pgres']['password'],
        database=cfg['pgres']['db'],
        port=cfg['pgres']['port'])

with conn_pg.cursor() as cursor_pg:
    sql = """
        SELECT * FROM leads;
    """
    cursor_pg.execute(sql)
    result = cursor_pg.fetchall()
    for r in result:
        leads.append({
            'first_name': r[1],
            'last_name': r[2],
            'email': r[3],
            'gender': None,
            'tags': r[6],
            'phone': r[4],
            'employer': r[5]
        })

keys = leads[0].keys()
with open('leads.csv', 'w') as outfile:
    dict_writer = csv.DictWriter(outfile, keys)
    dict_writer.writeheader()
    dict_writer.writerows(leads)
