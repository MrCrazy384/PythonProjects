n = int(input())
for i in range(1, n + 1):
    print(f"+___ ", end="")
print()
for i in range(1, n + 1):
    print(f"|{i} / ", end="")
print()
for i in range(n):
    print("|__\\ ", end="")
print()
for i in range(n):
    print("|    ", end="")
print()