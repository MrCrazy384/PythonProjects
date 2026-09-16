while True:
    try:
        n = []
        q = int(input())
        w = int(input())
        e = int(input())
        n.append(q)
        n.append(w)
        n.append(e)
        n.sort()
        print(n[-1], n[0], end=" ")
        n.pop(0)
        n.pop(-1)
        print(*n)
    except ValueError:
        break
