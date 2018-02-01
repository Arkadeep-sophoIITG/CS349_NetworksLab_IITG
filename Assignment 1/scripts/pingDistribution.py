import subprocess
import csv
import time
import matplotlib.pyplot as plt
import numpy as np


data1=[]
data2 =[]
cnt = 0
flag=False
with open('ques3a.txt','r') as f:
    for line in f:
        if line.startswith('64 bytes'):
            flag=True
            rob = line [-9:]
            robin = rob[:-3]
            data1.append(float(robin))
            
# with open("out1.txt","w") as txt1:
# 	txt1.write("\n".join(data1))



with open('ques3b.txt','r') as f:
    for line in f:
        if line.startswith('64 bytes'):
            flag=True
            rob = line [-9:]
            robin = rob[:-3]
            data2.append(float(robin))

# with open("out2.txt","w") as txt2:
# 	txt2.write("\n".join(data2))

plt.hist(data1, bins =75,normed=True)

plt.xlabel('Ping times')
plt.ylabel('Frequency')
plt.title('Histogram for ping -n 172.16.68.38')
plt.savefig('1.png')
plt.clf()

plt.hist(data2, bins =75,normed=True)

plt.xlabel('Ping times')
plt.ylabel('Frequency')
plt.title('Histogram for ping -p ff00 172.16.68.38')
plt.savefig('2.png')
plt.clf()	

