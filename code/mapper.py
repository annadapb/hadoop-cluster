#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0].strip().lower() == "series title": continue

    try:
        platform = row[5].strip().lower()
        rating = float(row[2].strip())
        if platform.lower() == "netflix": print("1 %lf"%rating)

    except (IndexError, ValueError): continue

