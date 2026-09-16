while True:
    try:
        n = int(input())
        q = n%10
        if q == 5:
            print("True")
        else:
            print("False")
    except ValueError:
        break
