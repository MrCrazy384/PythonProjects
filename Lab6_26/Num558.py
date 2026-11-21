n = int(input())
w = {}
for i in range(n):
    a, b = input().split()
    w[a] = b
    w[b] = a
q = input()
print(w[q])