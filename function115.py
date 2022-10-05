def landform(h):
    hs = sorted(h)
    if hs[0] != hs[1] and hs[0] != h[0] and hs[0] != h[-1]:
        return "valley"
    if hs[-1] != hs[-2] and hs[-1] != h[0] and hs[-1] != h[-1]:
        return "mountain"

#example      
print(landform([-3,34,567,6,-3]))          
