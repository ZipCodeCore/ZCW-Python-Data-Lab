#!/usr/bin/env python
import MySQLdb as mariadb
import psycopg2 as pgsql
import yaml
import csv
import uuid;

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

tags = {}
leads_tags = []

def id_for_tag(t):
    if (t in tags):
        return tags[t]
    else:
        tags[t] = uuid.uuid4()

conn = mariadb.connect(host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['password'],
        db=cfg['mysql']['db'],
        port=cfg['mysql']['port'])

leads = []
mariadb_tags_table = {}
with conn.cursor() as cursor:
    sql = """
        SELECT * FROM proleads;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        leads.append({
            'lead_id': uuid.uuid4(),
            'first_name': r[1],
            'last_name': r[2],
            'email': r[3],
            'gender': r[4],
            'phone': None,
            'employer': None,
            'tags': r[5]
        })

    tag_sql = """
        SELECT * FROM tags;
    """
    cursor.execute(tag_sql)
    t_result = cursor.fetchall()
    for t in t_result:
        mariadb_tags_table[t[0]] = t[1]

for lead in leads:
    for t in lead['tags'].split(","):
        try:
            t_name = mariadb_tags_table[t]
        except:
            t_name = "unknown"

        leads_tags.append({
            'lead_id': lead['lead_id'],
            'tag_id': id_for_tag(t_name)
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
        new_lead = {
            'lead_id': uuid.uuid4(),
            'first_name': r[1],
            'last_name': r[2],
            'email': r[3],
            'gender': None,
            'phone': r[4],
            'employer': r[5],
            'tags': r[6]
        }
        leads.append(new_lead)
        for t in r[6].split(" "):
            tag_id = id_for_tag(t)
            leads_tags.append({
                'lead_id': new_lead['lead_id'],
                'tag_id': tag_id
            })

lead_keys = leads[0].keys()
with open('leads.csv', 'w') as lead_file:
    dict_writer = csv.DictWriter(lead_file,lead_keys)
    dict_writer.writeheader()
    dict_writer.writerows(leads)

with open('tags.csv', 'w') as tag_file:
    writer = csv.writer(tag_file)
    writer.writerow(['name', 'tag_id'])
    for key, value in tags.items():
       writer.writerow([key, value])

leads_tags.pop(0)
leads_tags_keys = leads_tags[0].keys()
with open('lead_tag.csv', 'w') as leads_tag_file:
    dict_writer = csv.DictWriter(leads_tag_file, leads_tags_keys)
    dict_writer.writeheader()
    dict_writer.writerows(leads_tags)

