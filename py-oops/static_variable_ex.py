class A:
    variable = 'Static/class Variable'  # static/class variable
    var = 'Static/class Var'  # static/class variable

    def __init__(self):
        self.variable = 'Instance Variable'

    def foo(self):
        print(A.variable, self.variable)


print(A.variable)

a = A()
print(a.variable)
print(a.var)
a.foo()
