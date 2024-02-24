def mergeAlt(w1: str, w2: str) -> str:
    sol = []
    if (w1>w2):
        for w in w1:
            sol.append(w)
        for w in w2:
            sol.append(w)
    return sol

w1 = 'mike'
w2 = 'denver'
n = mergeAlt(w1, w2)
print (n)