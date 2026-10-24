s = input()
w = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        w += 1
    else:
        if w > 1:
            print(w, s[i - 1], sep="", end="")
        else:
            print(s[i - 1], end="")
        w = 1
if w > 1:
    print(w, s[-1], sep="", end="")
else:
    print(s[-1], end="")