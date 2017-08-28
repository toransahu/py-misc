class A:
     def __init__(self,x):
         self.x = x
     def spam(self,y):
        print (self.x, y)
s1 = A.spam # where s is referred as method of class A (here s1 in noth bound to any instance of class A, i.e. it is unbound)
a1 = A(5) # created an instance of class A
s1(a1,'Y') #calling method spam using unbound method s, we have to pass first argument an instance of class A


a2 = A(10) # created another instance of class A
s2 = a2.spam # here s2 is referred as method of class A, but it is bound to instance a2
s2('Y') # here s2 will pick a2 instance automatically to invoke spam method
