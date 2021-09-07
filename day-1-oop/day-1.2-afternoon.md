# Flow control
We use flow control to do exactly what the name suggests - we want to control the flow of the programme. 

Note that if you're coming from an ```R``` background, some of this might seem a little bit unusual. Don't worry, it gets to be second nature!

## For loops

    colours = ["red", "green", "blue"]
    # for each colour in the list called colours
    for colour in colours:
        print(colour)

### Increment decrement

    # create variable
    i = 0
    i += 1
    print(i)

### Comprehensions

In the above example, we are just printing each entry in a list. But let's say we wanted to do something to each of those entries and save the modified values to a new list:

    shouty_colours = []
    for colour in colours:
        upper_string = colour.upper()
        shouty_colours.append(upper_string)
    print(shouty_colours)

This can be made much more concise by using list comprehensions:

    # one liners baby!
    shouty_colours = [colour.upper() for colour in colours]

### Enumerate()

    for idx,i in enumerate(range(0,10)):
        print(f"Index:{idx}, Value:{i}")

    for idx,i in enumerate(range(0,10,2)):
        print(f"Index:{idx}, Value:{i}")

### while

    i = 10
    while i >= 5:
        print(i)
        i -= 1
        print("still counting...")
        if i < 5:
            print("done!")
            break

### if, elif, else

    for i in range(0,20):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

    for colour in colours:
        if colour == "red":
            pass
        elif colour == "green":
            print("ugly colour!")
        else:
            print("whatever")

## Exception handling
https://docs.python.org/3/tutorial/errors.html

    for colour in colours:
        try:
            print(colour//2)
        except:
            print("Wrong data type, ya jabrony!")

    for colour in colours:
        try:
            print(word)
        except NameError:
            print("No name, loser")


## Defining functions

    def hello():
        print("Hello, world!")

    def hello(name="Ross"):
        print(f"Hello, {name}!")

    def hello(name:str="Ross") -> str:
        print(f"Hello, {name}!")

## Return values

    def hello(name:str = "Ross", age:int = 31) -> str:
        return f"Hello, my name is {name}. I am {age} years old!"

## Importing packages

    import os
    inpath = os.path.join("..", "data")
    folder = os.listdir(inpath)

### Task

Create a function which does the following:

- Go to the folder called "data"
- For each file in a sorted list
  - check it is a csv
  - print the index and the filename
  - create a dictionary where keys=index and values = filename
  - return the dictionary to a variable

### Solution

    # just an example - notice use of type hints
    def parser(inpath:str) -> dict:
        """
        Takes an input filepath and returns a dict of filenames

        inpath:     The target filepath
        dictionary: A dict of {index:filename} pairs
        """
        # initialise empty dict
        dictionary = {}
        # get list of files in inpath folder
        folder = os.listdir(inpath)
        # get index and filename for each file
        for idx,file in enumerate(sorted(folder)):
            # if it is a csv file
            if file.endswith(".csv"):
                # print to display
                print(f"Working on {idx} called {file}")
                # update dictionary
                dictonary[idx] = file
            # if not csv, ignore
            else:
                pass
        return dictionary


## Classes

    class Person:
        species = "Homo sapiens"
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def welcome(self):
            print(f"Hello, my name is {self.name}!")

        def describe(self):
            print(f"I am {self.age} year old member of the species {self.species}")

    p1.age = 40