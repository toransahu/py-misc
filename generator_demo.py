def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1

print()
for i in first_n(5):
    print(i)

