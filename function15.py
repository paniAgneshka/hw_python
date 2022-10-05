def unique(s1, s2):
    a1 = set()
    a2 = set()
    for c in s1:
        a1.add(c)
    for c in s2:
        a2.add(c)
    comm = [c for c in a1 & a2]
    un1 = [c for c in a1 - a2]
    un2 = [c for c in a2 - a1]
    return comm, un1, un2

#example
print(unique("stht","aetjhet"))    
