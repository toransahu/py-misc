class A:
    static_variable = 'Static/class Variable of class A'  # static/class variable

    def __init__(self):
        self.instance_variable = 'Instance Variable'

    @classmethod
    def class_method(cls):
        print('Inside class_method()', cls.static_variable)  # works
        # print('Inside class_method()', cls.instance_variable)  # error, class method can't access instance attributes

    # static method
    def way2(cls):
        pass

    # making way2() a static method
    way2 = classmethod(way2)


class B(A):
    static_variable = 'Static/class Variable of class B'  # static/class variable


# but a module level func can access an instance attribute
def module_level_func():
    a1 = A()
    print(a1.instance_variable)


a2 = A()

a2.class_method()
A.class_method()
B.class_method()  # now it will access static variable of class B

