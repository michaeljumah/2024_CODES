def mergeAlt(w1: str, w2: str) -> str:
    sol = []
    sol1 = ''
    if (w1>w2):
        for w in w1:
            sol.append(w)
            sol1 = sol1 + w
              
        sol1 = sol1 + ' '
        for w in w2:
            sol.append(w)
            
            sol1 = sol1 + w
    return sol1

w1 = 'mike'
w2 = 'denver'
n = mergeAlt(w1, w2)
print (n)
