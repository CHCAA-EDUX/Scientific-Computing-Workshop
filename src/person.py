class Person:
    species = "Homo sapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print(f"Hello, my name is {self.name}!")

    def describe(self):
        print(f"I am {self.age} year old member of the species {self.species}")

if __name__=="__main__":
    person1 = Person("Ross", 31)