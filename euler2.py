

def fib(n):
    f0, f1 = 0, 1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0+f1


fibs = list(fib(100))
even_fibs = []
for f in fibs:
    if f < 4000000:
        if f % 2 == 0:
            even_fibs.append(f)

print(sum(even_fibs))
