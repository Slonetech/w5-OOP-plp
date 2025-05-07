class Person:
    def __init__(self, name, age):
        self.name = name          # public
        self.__age = age          # private (with __)

    def get_age(self):
        return self.__age         # accessing private attribute

    def set_age(self, age):
        if age > 0:
            self.__age = age

p = Person("Alice", 30)
print(p.get_age())               # Output: 30