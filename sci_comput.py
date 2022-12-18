import numpy as np
import scipy.optimize
import time
import math
from matplotlib import pyplot as plt
from random import randint
import matplotlib

class Lists(list):
    def __init__(self, lst):
        super().__init__(lst)
        
    def __mul__(self, other):
        return Lists(self[_]*other[_] for _ in range(len(self)))  

def average(lst):
    print(lst)
    print(sum(lst))
    print(len(lst))
    return sum(lst) / len(lst)
    
def approx(f, x, y, n):
    args, _ = scipy.optimize.curve_fit(f, x, y)
    lb = min(x)
    rb = max(x)
    h = (rb - lb) / n
    return [[lb + j * h for j in range(n)], [f(lb + i * h, *(__ for __ in args)) for i in range(n)]]
    
n=10000000

list_size = []
average_time= []
sigma = []
plt.subplot(2, 1, 1)
#plt.xlabel("list length")
plt.ylabel("t, s")
plt.title("List multiplication")

for j in range(1,n,math.ceil(n/10)):                    #list multiplication
    list_size.append(j)
    A_l=Lists([randint(10,100)]*j)
    B_l=Lists([randint(10,100)]*j)
    calculating_time = []
    for i in range(10):
        t1=time.time()
        A_l * B_l
        t2=time.time()
        calculating_time.append(t2-t1)
        print(t2 - t1)
    average_time.append(average(calculating_time))
    print(f"size {j}: {average_time[-1]}", end="")
    sigma.append(math.sqrt(average([(calculating_time[_] - average_time[-1]) ** 2 for _ in range(len(calculating_time))])))
    print(f"  sigma: {sigma[-1]}")

plt.errorbar(list_size, average_time, yerr=sigma, fmt="o", ecolor="#C79FEF", capsize=5, color="#C79FEF", label=f"{1}-dimension list")
plt.legend(fontsize=10)
curve = approx((lambda x, k, m: k * x + m), list_size, average_time, 100)
plt.plot(curve[0], curve[1], color="#C79FEF")

list_size = []
average_time= []
sigma = []
for j in range(1,math.ceil((n)**(1./2.)),math.ceil(n**(1./2.)/10.)):
    list_size.append(j*j)
    A_l=Lists([Lists([randint(10,100)]*j) for _ in range(j)])
    B_l=Lists([Lists([randint(10,100)]*j) for _ in range(j)])
    calculating_time = []
    for i in range(10):
        t1=time.time()
        A_l * B_l
        t2=time.time()
        calculating_time.append(t2-t1)
        print(t2 - t1)
    average_time.append(average(calculating_time))
    print(f"size {j}: {average_time[-1]}", end="")
    sigma.append(math.sqrt(average([(calculating_time[_] - average_time[-1]) ** 2 for _ in range(len(calculating_time))])))
    print(f"  sigma: {sigma[-1]}")

plt.errorbar(list_size, average_time, yerr=sigma, fmt="o", ecolor="#7BC8F6", capsize=5, color="#7BC8F6", label=f"{2}-dimension list")
plt.legend(fontsize=10)
curve = approx((lambda x, k, m: k * x + m), list_size, average_time, 100)
plt.plot(curve[0], curve[1], color="#7BC8F6")

list_size = []
average_time= []
sigma = []
for j in range(1,math.ceil((n)**(1./3.)),math.ceil(n**(1./3.)/10.)):
    list_size.append(j*j*j)
    A_l=Lists([Lists([Lists([randint(10,100)]*j) for _ in range(j)]) for _ in range(j)])
    B_l=Lists([Lists([Lists([randint(10,100)]*j) for _ in range(j)]) for _ in range(j)])
    calculating_time = []
    for i in range(10):
        t1=time.time()
        A_l * B_l
        t2=time.time()
        calculating_time.append(t2-t1)
        print(t2 - t1)
    average_time.append(average(calculating_time))
    print(f"size {j}: {average_time[-1]}", end="")
    sigma.append(math.sqrt(average([(calculating_time[_] - average_time[-1]) ** 2 for _ in range(len(calculating_time))])))
    print(f"  sigma: {sigma[-1]}")

plt.errorbar(list_size, average_time, yerr=sigma, fmt="o", ecolor="#76FF7B", capsize=5, color="#76FF7B", label=f"{3}-dimension list")
plt.legend(fontsize=10)
curve = approx((lambda x, k, m: k * x + m), list_size, average_time, 100)
plt.plot(curve[0], curve[1], color="#76FF7B")


plt.subplot(2, 1, 2)                                    #numpy-array multiplication
plt.xlabel("array length")
plt.ylabel("t, s")
plt.title("Numpy array multiplication")

list_size = []
average_time= []
sigma = []
for j in range(1, n, math.ceil(n/10)): 
    list_size.append(j)
    A_l=np.array(Lists([randint(10,100)]*j))
    B_l=np.array(Lists([randint(10,100)]*j))
    calculating_time = []
    for i in range(10):
        t1=time.time()
        A_l * B_l
        t2=time.time()
        calculating_time.append(t2-t1)
        print(t2 - t1)
    average_time.append(average(calculating_time))
    print(f"size {j}: {average_time[-1]}", end="")
    sigma.append(math.sqrt(average([(calculating_time[_] - average_time[-1]) ** 2 for _ in range(len(calculating_time))])))
    print(f"  sigma: {sigma[-1]}")

plt.errorbar(list_size, average_time, yerr=sigma, fmt="o", ecolor="#C79FEF", capsize=5, color="#C79FEF", label=f"{1}-dimension list")
plt.legend(fontsize=10)
curve = approx((lambda x, k, m: k * x + m), list_size, average_time, 100)
plt.plot(curve[0], curve[1], color="#C79FEF")

list_size = []
average_time= []
sigma = []
for j in range(1,math.ceil((n)**(1./2.)),math.ceil(n**(1./2.)/10.)):
    list_size.append(j*j)
    A_l=np.array(Lists([Lists([randint(10,100)]*j) for _ in range(j)]))
    B_l=np.array(Lists([Lists([randint(10,100)]*j) for _ in range(j)]))
    calculating_time = []
    for i in range(10):
        t1=time.time()
        A_l * B_l
        t2=time.time()
        calculating_time.append(t2-t1)
        print(t2 - t1)
    average_time.append(average(calculating_time))
    print(f"size {j}: {average_time[-1]}", end="")
    sigma.append(math.sqrt(average([(calculating_time[_] - average_time[-1]) ** 2 for _ in range(len(calculating_time))])))
    print(f"  sigma: {sigma[-1]}")

plt.errorbar(list_size, average_time, yerr=sigma, fmt="o", ecolor="#7BC8F6", capsize=5, color="#7BC8F6", label=f"{2}-dimension list")
plt.legend(fontsize=10)
curve = approx((lambda x, k, m: k * x + m), list_size, average_time, 100)
plt.plot(curve[0], curve[1], color="#7BC8F6")

list_size = []
average_time= []
sigma = []
for j in range(1,math.ceil((n)**(1./3.)),math.ceil(n**(1./3.)/10.)):
    list_size.append(j*j*j)
    A_l=np.array(Lists([Lists([Lists([randint(10,100)]*j) for _ in range(j)]) for _ in range(j)]))
    B_l=np.array(Lists([Lists([Lists([randint(10,100)]*j) for _ in range(j)]) for _ in range(j)]))
    calculating_time = []
    for i in range(10):
        t1=time.time()
        A_l * B_l
        t2=time.time()
        calculating_time.append(t2-t1)
        print(t2 - t1)
    average_time.append(average(calculating_time))
    print(f"size {j}: {average_time[-1]}", end="")
    sigma.append(math.sqrt(average([(calculating_time[_] - average_time[-1]) ** 2 for _ in range(len(calculating_time))])))
    print(f"  sigma: {sigma[-1]}")

plt.errorbar(list_size, average_time, yerr=sigma, fmt="o", ecolor="#76FF7B", capsize=5, color="#76FF7B", label=f"{3}-dimension list")
plt.legend(fontsize=10)
curve = approx((lambda x, k, m: k * x + m), list_size, average_time, 100)
plt.plot(curve[0], curve[1], color="#76FF7B")

fig = plt.gcf()
fig.set_size_inches(12, 6.5)
fig.savefig("test.png", dpi=250)
plt.show()

