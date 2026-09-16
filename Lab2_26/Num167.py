while True:
    try:
        n = int(input())
        q = n/10
        if (q < 10) & (q >= 1):
            print("True")
        else:
            print("False")
    except ValueError:
        break