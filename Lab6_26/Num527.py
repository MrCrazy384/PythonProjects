q = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
w = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
e = dict(zip(q, w))
n = input().strip().upper()
print(e.get(n))