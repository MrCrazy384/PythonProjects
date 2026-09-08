while True:
    try:
        n = int(input())
        q = n % 10
        w = n - q
        w = w / 10
        print(int(w))
    except ValueError:
        break