e = int(input())
q = int(input())
r = str(input())
w = []
for i in range(e):
    a = input()
    if len(a) == q:
        a = a[:-3] + r
    w.append(a)
print("\n".join(w))