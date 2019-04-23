#!/usr/bin/env python3
from pyexcel_ods import get_data
import os

data = get_data("/Users/adolf/Documents/issue/issue.ods")
count = 0
for line in data['Sheet1']:
    fo = open(f'/tmp/issue_{count}.txt', "w")
    print(line)
    title = line[7] if 7 < len(line) else ""
    img = line[11] if 11 < len(line) else ""
    pm = line[14] if 14 < len(line) else ""
    dev = line[15] if 15 < len(line) else ""

    prio = line[1] if 1 < len(line) else ""
    tag = line[10] if 10 < len(line) else ""

    fo.write(title)
    fo.write("\n\n\n")
    fo.write(f'img:{img}\n\nPM:{pm}\n\nDEV:{dev}\n\n')
    fo.close()

    os.system(f'hub issue create -F /tmp/issue_{count}.txt -l{prio},{tag}')
    print(f'hub issue create -F /tmp/issue_{count}.txt -l{prio},{tag}')
    count=count+1

