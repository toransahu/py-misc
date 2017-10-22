def foo(*args, **kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)

foo(1,2,v1='car', v2='bike')
