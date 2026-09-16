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
        print(*n)
    except ValueError:
        break
