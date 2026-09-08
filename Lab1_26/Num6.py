while True:
    try:
        n = int(input())
        q = n % 10
        print(q)
    except ValueError:
        break