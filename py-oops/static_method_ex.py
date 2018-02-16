class A:
    static_variable = 'Static/class Variable of class A'  # static/class variable

    def __init__(self):
        self.instance_variable = 'Instance Variable'

    @staticmethod
    def static_method():
        print('Inside static_method()', A.static_variable)  # works
        # print('Inside static_method()', A.instance_variable)  # error, static method can't access instance attributes

    # static method
    def way2():
        pass

    # making way2() a static method
    way2 = staticmethod(way2)


class B(A):
    static_variable = 'Static/class Variable of class B'  # static/class variable


# but a module level func can access an instance attribute
def module_level_func():
    a1 = A()
    print(a1.instance_variable)


a2 = A()

a2.static_method()
A.static_method()
B.static_method()  # will access static variable of class A

