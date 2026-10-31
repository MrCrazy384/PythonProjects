q = list(map(int, input().split()))
w = max(q, key=q.count)
print(w)