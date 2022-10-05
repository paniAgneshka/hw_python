def bracket_grouping(str):
    i = 0
    res = []
    l = 0
    for j in range(len(str)):
        if str[j] == '(':
            i += 1
        elif str[j] == ')':
            i -= 1
        if i == 0:
            res.append(str[l:(j + 1)])
            l = j + 1
    return res

#example
print(bracket_grouping("(())()"))        
