q = list(map(int, input().split()))
while " " in q:
    q.remove(" ")
w = []
for i in range(len(q)):
    if i ==len(q)-1:
        e = q[i-1] + q[0]
        w.append(e)
    else:
        e = q[i-1] + q[i+1]
        w.append(e)
print(" ".join(map(str, w)))
