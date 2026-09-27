n = {1000: "Volodymur Vernadsuy",
     500: "Grigory Skovoroda",
     200: "Lesya Ykrainka",
     100: "Taras Shevchenko",
     50: "Mukhailo Grushevsy",
     20: "Ivan Franko",
     10: "Ivan Mazepa",
     5: "Bohdan Khmelnutsky",
     2: "Yaroslav Mudruy",
     1: "Volodymur Velukuy",}
while True:
    try:
        q = int(input())
        if q in n:
            print(f"{q}, {n[q]}")
        else:
            print("No Bill")
    except ValueError:
        break