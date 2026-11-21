desk = []
for i in range(8):
    desk.append(["."] * 8)
q = input()
a = ord(q[0]) - ord("a")
b = int(q[1]) - 1
desk[b][a] = "O"
moves = [
    (0, 1), (0, -1),
    (1, 0), (-1, 0),
    (1, 1), (1, -1),
    (-1, 1), (-1, -1)
]
for x, y in moves:
    i = b + y
    j = a + x
    while 0 <= i < 8 and 0 <= j < 8:
        desk[i][j] = "*"
        i += y
        j += x
for row in desk[::-1]:
    print(" ".join(row))