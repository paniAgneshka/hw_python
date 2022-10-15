def landform(h):
    dh = []
    ddh = []
    for i in range(len(h) - 1):
        dh.append(h[i + 1] - h[i])
    for i in range(len(dh) - 1):
        ddh.append(dh[i] * dh[i + 1])
    peak = 0
    num_peaks = 0
    for i in range(len(ddh)):
        if ddh[i] < 0:
            peak = i
            num_peaks += 1
    if num_peaks == 1:
        if h[peak + 1] - h[0] > h[-1] - h[peak + 1]:
            return "Hill"
        elif h[peak + 1] - h[0] < h[-1] - h[peak + 1]:
            return "Valley"
          
    
#example      
print(landform([-3,34,567,123,23,16,-2]))                 
print(landform([-3,34,567,6,-2, 5, 54, 2, -4]))
print(landform([321, 34, 5, 6, 24]))
