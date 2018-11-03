import random

box = []
values = []
for j in range(0,100):
    for i in range(0,1000):
        a = random.randint(1,5)
        if a not in box:
            box.append(a)
        if len(box) == 5:
            print(i)
            values.append(i)
            box = []
            break

import csv

with open('data.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(values)