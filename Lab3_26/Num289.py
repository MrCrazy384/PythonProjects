n = int(input())
t = 0
w = 1
for j in range(n):
    for i in range(w):
        q = w - i
        if w%q == 0:
            t += 1
    print(w, "+" * t, sep="")
    t = 0
    w += 1