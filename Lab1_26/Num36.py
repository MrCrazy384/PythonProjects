while True:
    try:
        a = int(input())
        b = int(input())
        q = a/b
        w = b/a
        print(f"{q:9.5f}***", f"{w:9.5f}")
    except ValueError:
        break
