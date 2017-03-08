def fib3(n1, n2, cnt):
    if cnt == 0:
        return n1 + n2
    else:
        return fib3(n2, n1 + n2, cnt - 1)

def fib(n):
    if n == 0:
        return 0

    if n <= 2:
        return 1

    return fib3(1, 1, n - 3)
