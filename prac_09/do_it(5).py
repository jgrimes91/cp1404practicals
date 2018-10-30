def run(n):
    # for n in range(n):
        if n <= 0:
            run(n - 1)
            print(n)

run(5)