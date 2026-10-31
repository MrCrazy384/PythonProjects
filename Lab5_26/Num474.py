q = int(input())
for j in range(q // 2):
    print(" ".join(["."]*j+["*"]+["."]*(q//2-j-1)+["*"]+["."]*(q//2-j-1)+["*"]+["."]*j))
print(" ".join(["*"] * q))
for j in range(q // 2):
    print(" ".join(["."]*(q//2-j-1)+["*"]+["."]*j+["*"]+["."]*j+["*"]+["."]*(q//2-j-1)))