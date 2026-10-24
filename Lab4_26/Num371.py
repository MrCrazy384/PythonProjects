n= input()
w = input()
i = []
for j in range(len(n)):
    if n[j] == w:
        i.append(j)
if i:
    print(i[0], i[-1])
