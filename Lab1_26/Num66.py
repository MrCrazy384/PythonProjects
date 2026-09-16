while True:
    try:
        n = int(input())
        k = int(input())
        k = 10 ** k
        q = n % k
        n = n - q
        n = n / k
        print(int(q))
    except ValueError:
        break
