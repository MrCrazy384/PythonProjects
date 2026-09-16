while True:
    try:
        n = int(input())
        b = bin(n)
        b = str(b)
        b = b[2:]
        q = b[::-1]
        if q == b:
            print("True")
        else:
            print("False")
    except ValueError:
        break