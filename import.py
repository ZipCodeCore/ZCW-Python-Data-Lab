#!/user/bin/env python
import csv

with open("leads.csv") as infile:
    leads = csv.DictReader(infile)
    for lead in leads:
        print(lead['email'])

