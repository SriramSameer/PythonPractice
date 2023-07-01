# Person

# Data Member

# Methods - Behav

class Person:
    name = None
    age = None
    email_id = None

    def __int__(self, name, age, email_id):
        self.name = name
        self.age = age
        self.email_id = email_id

    def sleep(self):
        print(self.name + " is sleeping")

    def eating(self):
        print(self.name + " is Eating")


pramod = Person("Pramod", "32", "p@d.com")
print(pramod.name)
pramod.eating()
pramod.sleep()


amit = Person("Amit", "32", "a@d.com")
amit.sleep()

