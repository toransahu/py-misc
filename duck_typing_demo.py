"""
* EAFP: Easier to Ask Forgiveness than Permission
* Tag line definition: If an object can quack & fly, then its a duck.
* Do not worry about, if this object has this attribute or not, just try it inside try: block. If work then great, else handle the error.
"""


class Duck:
    def quack(self):
        print("Quack quack")

    def fly(self):
        print("Flap flap")


class Person:
    def quack(self):
        print("I can mimic quack quack")

    def fly(self):
        print("I can flap my arms")


# non-pythonic (LBYL: Look Before You Leap)
def quack_and_fly(entity):
    if hasattr(entity, 'quack'):
        if callable(entity.quack):
            entity.quack()

    if hasattr(entity, 'fly'):
        if callable(entity.fly):
            entity.fly()


# pythonic: EAFP: Easier to Ask Forgiveness than Permission
def quack_and_fly_pythonic(entity):
    try:
        entity.quack()
        entity.fly()
    except AttributeError as e:
        print(e)


duck = Duck()
person = Person()

quack_and_fly(duck)
print()
quack_and_fly(person)


# Example 2
emp = {'name': 'toran', 'age': 26, 'mobile': '8602431733'}
try:
    print("My name is {name} and I'm {age} years old. I am a {job}. You can contact me at {mobile}.".format(**emp))
except KeyError as e:
    print("Missing {} key".format(e))