def fibonacci_func(n):
    a,b = 0, 1
    i = 0
    print("call")
    while True:
        if (i > n):    return
        print("yield")
        yield a
        a, b = b, a+b
        print("a %d", a)
        print("b %d", b)
        print("i %d", i)
        print("-----------------")
        i += 1

fib = fibonacci_func(10)
for x in fib:
    print(x)

