import subprocess
import csv
import time

subnet_range = '172.16.68.59/26' 
command = 'nmap -n -sP ' + subnet_range +'> nmap2.txt'
k = subprocess.call(command,shell= True)
data=[]
cnt = 0
flag=False
with open('nmap2.txt','r') as f:
    for line in f:
        if line.startswith('Nmap scan report for '):
            flag=True
            cnt=cnt+1
        if flag:
            data.append(line.strip('Nmap scan report for '))
        flag = False

resultFile = open("results_nmap.txt",'a')
resultFile.write('\n------------------------\n')
resultFile.write(str(time.strftime("%d %b %Y %H:%M:%S" , time.localtime())))
resultFile.write('\n-----------------------\n')
resultFile.write(str(cnt))

	

