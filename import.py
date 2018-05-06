#!/user/bin/env python
import csv
import MySQLdb as mysql
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

leads = []
with open("leads.csv") as infile:
    rows = csv.DictReader(infile)
    for row in rows:
        leads.append(row)

tags = []
with open("tags.csv") as t_infile:
    t_rows = csv.DictReader(t_infile)
    for row in t_rows:
        tags.append(row)

lead_tag = []
with open("lead_tag.csv") as lt_infile:
    lt_rows = csv.DictReader(lt_infile)
    for row in lt_rows:
        lead_tag.append(row)

conn = mysql.connect(host=cfg['merge']['host'],
        user=cfg['merge']['user'],
        passwd=cfg['merge']['password'],
        db=cfg['merge']['db'],
        port=cfg['merge']['port'])

conn.cursor().executemany("""
    INSERT INTO leads (lead_id, first_name, last_name, email, gender, employer, phone)
    VALUES (%(lead_id)s,
            %(first_name)s,
            %(last_name)s,
            %(email)s,
            %(gender)s,
            %(employer)s,
            %(phone)s)""", leads)

conn.cursor().executemany("""
        INSERT INTO tags (tag_id, name)
        VALUES (%(tag_id)s,
                %(name)s)""",tags)

conn.cursor().executemany("""
        INSERT INTO lead_tag (lead_id, tag_id)
        VALUES (%(lead_id)s,
                %(tag_id)s)""",lead_tag)
conn.commit()
