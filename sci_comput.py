import numpy as np
import time
import math
from matplotlib import pyplot as plt
from random import randint

n=100

A_arr1=np.random.randint(low=10, high=100, size=(1,n))
B_arr1=np.random.randint(low=10, high=100, size=(1,n))
#print(A_arr1)

#print(A_l1)

A_arr2=np.random.randint(low=10, high=100, size=(2,n))
B_arr2=np.random.randint(low=10, high=100, size=(2,n))

#A_l2=[[randint(10,100)]*n for _ in range(2)]
#B_l2=[[randint(10,100)]*n for _ in range(2)]


A_arr3=np.random.randint(low=10, high=100, size=(3,n))
B_arr3=np.random.randint(low=10, high=100, size=(3,n))

#A_l3=[[randint(10,100)]*n for _ in range(3)]
#B_l3=[[randint(10,100)]*n for _ in range(3)]

calculating_time = []
list_size = []
average_time= []
sigma = []
for m in range(3):
    for j in range(n):
        list_size.append(j+1)
        A_l=[[randint(10,100)]*(j+1) for _ in range(m+1)]
        B_l=[[randint(10,100)]*(j+1) for _ in range(m+1)]
        for i in range(10):
            t1=time.time()
            for k in range(0,len(A_l)):
                A_l[k]*B_l[k]
            t2=time.time()
            calculating_time.append(t2-t1)
        average_time.append(sum(calculating_time)/len(calculating_time))    
        sigma.append(math.sqrt(average([(calculating_time[_] - average_time) ** 2 for _ in range(len(calculating_time))])))
