while True:
    try:
        n = int(input())
        i = 0
        q = 0
        for i in range (n+1):
            q = q + i*i
        print(q)
    except ValueError:
        break