# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Person:
    name = ""
    age = 0
    city = ""

    def walk(self):
        speed = 50
        print('{} is walking at {} mph'.format(self.name, speed))
        print(locals())

sailor1 = Person()
sailor1.name = "curtis"
sailor1.age = 30
sailor1.city = 'Portsmouth'
sailor1.walk()

sailor2 = Person()
sailor2.name = "david"
sailor2.age = 50
sailor2.city = 'London'
sailor2.walk()

sailor3 = sailor2
sailor3.walk()
speed = 1000
print(locals())
sailor1.name = 'fred'

sailor1.speed = 200


class Type45:
    name = ""
    length = 150
    guns = ""
    missiles = 32

#print(locals())
