fileID = fopen('out1.txt','r');
formatSpec = '%f'
a = fscanf(fileID,formatSpec);
%min(a)
%max(a)
a=sort(a);
x  = 0:0.5:165;
subplot(2,1,1)
histfit(a,500);
xlabel('Ping latency range')
ylabel('Frequecy')
xlim([0,1.2])
title('For ping -c 1000 -n 172.16.68.59') 
subplot(2,1,2)
histfit(a,500)
title('For ping -c 1000 -n 172.16.68.59 with log xscale') 
set(gca,'xscale','log')
xlabel('Ping latency range')
ylabel('Frequecy')
disp('median1')
disp(median(a))

fileID = fopen('out2.txt','r');
formatSpec = '%f'
a = fscanf(fileID,formatSpec);
%min(a)
%max(a)
a=sort(a);
x  = 0:0.5:165;
figure(2)
subplot(2,1,1)
histfit(a,500);
xlabel('Ping latency range')
ylabel('Frequecy')
xlim([0,1.1])
title('For ping -c 1000 -p ff00 172.16.68.59') 
subplot(2,1,2)
histfit(a,500)
set(gca,'xscale','log')

xlabel('Ping latency range')
ylabel('Frequecy')
title('For ping -c 1000 -p ff00 172.16.68.59 with log xscale') 
%xlim([0.1 1.1])
disp('median2')
disp(median(a))

