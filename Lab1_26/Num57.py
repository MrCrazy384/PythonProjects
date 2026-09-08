while True:
    try:
        q = float(input())
        w = q * 1000
        e = w * 0.4
        r = e * 0.7
        print(r)
    except ValueError:
        break
