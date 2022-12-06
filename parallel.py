from multiprocessing import Process
from time import time
from math import floor


def func(n):
    sum_ = 0
    for i in range(floor(n)):
        sum_ = sum_ + 1
    return sum_    

if __name__=='__main__':
    number = 30000000
    flow = 1
    lead_time = []
    while 1==1:
        processes = []
        for _ in range(flow):
            proc =Process(target=func, args=(number / flow, ))
            processes.append(proc)
        for proc in processes:
            proc.start()
        time_1 = time()
        for proc in processes:
            proc.join()
        time_2 = time()
        lead_time.append(time_2-time_1)   
        print(f"{flow} processes, {time_2-time_1} s")     
        if flow > 1:
            if lead_time[flow-2] < lead_time[flow-1]:
                break
        flow += 1        
    print(f"You have {flow - 1} cores", end=" ")
