n = int(input())
t = 0
for i in range(1, n+1):
    q = i
    w = int(str(q)[::-1])
    if q == w:
        t += 1
print(t)
