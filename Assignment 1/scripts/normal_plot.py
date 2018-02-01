import matplotlib.pyplot as plt

time = ['19:00:29','19:40:07','20:00:04','20:50:45','22:14:17']
num = [34,32,26,27,32]
plt.xlabel('Recorded time')
plt.ylabel('Number of hosts online')
x = range(5)
plt.xticks(x, time)
plt.plot(x,num,linewidth = 3, marker='*',markerfacecolor='green', markersize=12)
plt.savefig('hosts_online.png')
plt.clf()