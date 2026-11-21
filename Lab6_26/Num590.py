desk = []
for i in range(8):
    desk.append(["."] * 8)
q = input()
st = ord(q[0]) - ord("a")
r = int(q[1]) - 1
desk[r][st] = "K"
moves = [
    (2, 1), (2, -1),
    (-2, 1), (-2, -1),
    (1, 2), (1, -2),
    (-1, 2), (-1, -2)]
for x, y in moves:
    i = r + y
    j = st + x
    if 0 <= i < 8 and 0 <= j < 8:
        desk[i][j] = "*"
for z in desk[::-1]:
    print(" ".join(z))
