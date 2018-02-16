class Animal:
    def can_do(self):
        print("Can do anything")

    def can_do(self, i):
        print("Can do ",i)

a = Animal()
a.can_do("run")