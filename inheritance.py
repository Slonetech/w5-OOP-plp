class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):               # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()                        # Inherited method
d.bark()                         # Own method
