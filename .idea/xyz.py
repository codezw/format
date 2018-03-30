import csv
import numpy as np

with open(r"C:\Users\z\Desktop\xyz.csv") as c:
    r = csv.reader(c)

    x,y,z = [],[],[]
    for i in r:
        x.append(i[2])
        y.append(i[3])
        z.append(i[4])
