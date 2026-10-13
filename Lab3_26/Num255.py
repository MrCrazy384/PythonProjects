while True:
    try:
        t = 0
        n = int(input())
        for i in range (100, 1000):
            q = i%10
            w = int((i%100 - q)/10)
            e = int(i/100)
            r = q + w + e
            if r == n:
                t += 1
        print(t)
    except ValueError:
        break
