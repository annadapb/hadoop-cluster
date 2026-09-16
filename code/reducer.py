#!/usr/bin/env python

import sys

total_rating = .0
count = 0

for line in sys.stdin:
    if not line: continue
    line = line.strip()

    try:
        _, rating = line.split(' ', 1)
        total_rating += float(rating)
        count += 1

    except ValueError: continue

if count>0: print("Avg. Netflix Rating: %lf"%(total_rating/count))
