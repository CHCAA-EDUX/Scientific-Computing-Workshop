

## Classes

A class is a blueprint for creating objects. It defines the data and behavior of the objects that will be created from it.

For instance the following object is a class `Person`:

```python
class Person:
    species = "Homo sapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print(f"Hello, my name is {self.name}!")

    def describe(self):
        print(f"I am a {self.age} year old member of the species {self.species}")
```

We can use the class in the following way:

```python
kenneth = Person("kenneth", 28)  # calls the __init__ function
kenneth.welcome() 
kenneth.describe()
```
Which should output:

```
Hello, my name is Kenneth!
I am a 28 year old member of the species homo sapiens
```

Note that we do not need to pass in the `self` attribute. The class simply passed in the object itself.

A class in python typically consist of `methods` functions that you can call on the object such as `kenneth.describe()` or `attributes` such as `kenneth.age`. There are a few special `methods` such as `__init__` which takes on a special function. In this case it is called at initialization or creation of the object. 


## Exercise 1:
Create a class Table which takes in two list of values (columns). One of names and one of ages.

```python
table_obj = Table(names = ["kenneth", "anders", "scott"], ages = [28, 32, 5]) 
```

It should be able to get the mean age:
```python
mean_age = table_obj.mean_age()
```

It should be able to get the age for a specific person:
```python
anders_age = table_obj.get_age_of(name="anders")
```

And it should be able to print a table:
```python
table_obj.print_table()
```
Which could output a table on the form:

```
| Name    | Age |
| ------- | --- |
| kenneth | 28  |
| anders  | 32  |
| scott   | 5   |
```

You should not use any external libraries such as pandas or numpy.

## Play Around 1:

I can access the attributes age, species and name using the format `kenneth.{attribute}` e.g. `kenneth.age` or `kenneth.species`. In that way they seem similar, but why is it that age and name is assigned in the `__init__` function?


# Conceptual 1 (optional):
You might not believe me when I said that self is the same as the class instance. Well that is great. A large part of programming is being able to test these statements. In the following you see an example of how one would be able to test such as statement:

```python
class DummyClass:

    def __init__(self):
        self.random_variable = 1

    def test_is_self_the_class(self, class_obj):
        if self == class_obj:
            print("it is!")
        else:
            print("it is not!")
```

```python
obj = DummyClass()
obj.test_is_self_the_class(obj)
```

## Exercise 2 (optional):

Read up on the `__add__` method. What does it do? How can you use it?
Can you define add the `__add__` method to the Table class such that you can add two tables together?

```python
table_obj1 = Table(names = ["kenneth", "anders", "scott"], ages = [28, 32, 5])
table_obj2 = Table(names = ["john", "jane", "joe"], ages = [10, 20, 30])
table_combined = table_obj1 + table_obj2
```

## Exercise 3 (optional):

Create a class called `Group`, which takes in a list of `Person` object and can have them talk.
Talk

```python
kenneth = Person("kenneth", 28)
...
group = Group([kenneth, anders, scott])
group.talk("kenneth", "anders")
```

Which should print:

```
kenneth: Hello, my name is kenneth!
anders: Hello, my name is anders!
kenneth: I am a 28 year old member of the species homo sapiens
anders: ...
```


## Subclasses (optional):
Python classes also allow for subclasses. A class which inherits from another class.

For instance we might want an object `Student` which is the same as Person, except that it also has a degree.

```python
class Student(Person):
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
```

We can then run it using:

```python
kenneth = Student("kenenth", 28, "cogsci")
kenneth.welcome() # we can call methods that already exists
```
Which will print:
```
Hello, my name is kenneth!
```

We can also test if this is a person using:
```python
is_it_a_person = isinstance(keneth, Person)
print(is_it_a_person)
# True
```

What happen if you run?
```
is_it_a_person = type(kenneth) == "Person"
print(is_it_a_person)
```

Can you explain why that happens? 


We it also overwrite existing methods such that we use the new degree instead of the old one.
```python
class Student(Person):
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
    

    def describe(self):
        print(f"I am a {self.age} year old member of the species {self.species} and I am studying {self.degree}")
```

## Exercise 4 Making friends (optional):

Create a subclass of `Group` called `Party` in which each person becomes friends with each other after they talk.

```python
kenneth = Person("kenneth", 28)
anders = Person("anders", 32)
scott = Person("scott", 5)

party = Party([kenneth, anders, scott])

party.talk("kenneth", "anders")
party.friends("kenneth")
# ["anders"]

party.talk("kenneth", "scott")
party.friends("kenneth")
# ["anders", "scott"]
```



