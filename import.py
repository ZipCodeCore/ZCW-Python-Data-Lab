#!/user/bin/env python
import csv
import MySQLdb as mysql
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

leads = []
with open("leads.csv") as infile:
    rows = csv.DictReader(infile)
    print(type(result.))
    for row in rows:
        leads.append(row)

conn = mariadb.connect(host=cfg['mysql']['host'],
        user=cfg['mysql']['user'],
        passwd=cfg['mysql']['password'],
        db=cfg['mysql']['db'],
        port=cfg['mysql']['port'])
