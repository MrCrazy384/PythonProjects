w = str(input())
q = ""
for i in w:
    if i.isalpha():
        q += i
q = q.lower()
w = w.lower()
if q == q[::-1]:
    print("Yes")
else:
    print("No")