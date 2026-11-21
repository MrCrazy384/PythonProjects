q = [0] * 9
for i in map(int, input().split()):
    if i == 0:
        break
    q[i - 1] += 1
print(*q)