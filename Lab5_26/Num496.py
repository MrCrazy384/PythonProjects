q = list(map(int, input().split()))
w = int(input())
e = []
for i in range(len(q)):
    if q[i] == w:
        e.append(i+1)
print(" ".join(map(str, e)))