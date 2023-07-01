# Animal - Parent
# Dog is a type of animal - Child
class Animal:
    def speak(self):
        print("Animal Speak")


class Dog(Animal): # Child class has access to all the methods and variables
    def bark(self):
        print("Woof")


# myanimal = Animal()
# myanimal.speak()

mydog = Dog()
mydog.bark()
mydog.speak()