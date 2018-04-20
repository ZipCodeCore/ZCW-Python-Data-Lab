#!/usr/bin/env python
import MySQLdb as mysql
import psycopg2 as pgsql
import yaml

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


