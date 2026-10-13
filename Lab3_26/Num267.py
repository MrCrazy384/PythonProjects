n = int(input())
for i in range(n):
    r = ["-1"] * i + ["0"] + ["1"] * (n-i-1)
    print("\t".join(r))