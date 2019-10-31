# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x=[]
y=[]
y1=[]
y2=[]
for i in range(50):
#x = np.asarray([n for n in range(10)])
    x.append(i)
    y.append(np.random.randn(1))
    y1.append(np.random.randn(1))
    y2.append(np.random.randn(1))
    if len(x)>10:
        x = x[-10:]
        y = y[-10:]
        y1 = y1[-10:]
        y2 = y2[-10:]
    
#    print('x shape:{}, y shape:{}'.format(x.shape, y.shape))
#    print('y: {}\ny1: {}\ny2: {}'.format(y,y1,y2))
    
    plt.clf()
    
    plt.subplot(2,1,1)
    plt.plot(x, y, '-*', label='y')
    plt.ylabel('Temp (\'C)')
    plt.legend()
    
    plt.subplot(2,1,2)
    plt.plot(x, y1, '-*', label='y1')
    plt.plot(x, y2, '-*', label='y2')  
    plt.xlabel('Time')
    plt.ylabel('RAM Usage (MB)')
    
#    plt.title('sample plot')
    plt.legend()
    plt.show()
#    plt.savefig('plot.png')
