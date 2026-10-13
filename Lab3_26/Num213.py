while True:
    try:
        n = int(input())
        for i in range(n):
            print("#" + " " * i + "#")
    except ValueError:
        break