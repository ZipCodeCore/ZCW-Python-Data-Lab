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

conn = mysql.connect(host=cfg['merge']['host'],
        user=cfg['merge']['user'],
        passwd=cfg['merge']['password'],
        db=cfg['merge']['db'],
        port=cfg['merge']['port'])

conn.cursor().executemany("""
    INSERT INTO leads (first_name, last_name, email, gender, employer, phone, tags)
    VALUES (%(first_name)s,
            %(last_name)s,
            %(email)s,
            %(gender)s,
            %(employer)s,
            %(phone)s,
            %(tags)s)""", leads)
conn.commit()
