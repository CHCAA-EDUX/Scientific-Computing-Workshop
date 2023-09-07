# Scripting

This module is about scripting. We will learn about the basics of programming, and how to write simple programs in Python which are callable from the terminal.


## Learning Goals

- The student can write simple programs in Python
- The student can call a Python program from the terminal

## What is a Script?

A script is a program that is written in a scripting language (such as python). A scripting language is a programming language that supports scripts. Scripts are programs that are executed without the need for a compilation step. This means that you can write a script, and then run it directly without having to compile it first. This is in contrast to compiled languages, where you have to compile the program before you can run it.

## An example script:

Let us assume a file called `hello_world.py` with the following content:

```py
print("Hello World!")
```

This is a valid Python program. We can run it from the terminal like this:

```bash
$ python hello_world.py
Hello World!
```

You can even add more to it, such as functions:

```py
def present_python():
    print("Let me present Python!")
    print("It is a great language!")
    print("It can do many things such as:")

    thing_python_can_do = [
        "Web development",
        "Data science",
        "Machine learning"
    ]

print("Hello World!")
present_python()
```


```bash
$ python hello_world.py
Hello World!
Let me present Python!
...
```


## Exercises

In groups of 2-3, make the following exercises. Explain to each other why you answer as you do. For the programming exercises, all group members should be programming --> learning by doing! You do not learn programming by seeing other people type into a terminal!

### Exercise 1: Hello {Person}

Write a program, `hello.py` that says hello and asks for a name.
You should be able to run your program from the terminal.

**Hint!** To get user input, use the following:

```py
name = input()
```

Example:

```bash
$ python hello.py
What is your name? Harry
Hello Harry!
```

### Conceptuals (Optional)

0.0: What is the suggested naming practice for Python?

0.1: Why is `harry` a valid variable name and 100 invalid?

0.2: What does it mean that we have 0-based indexing in Python?

0.3: Name three data types.

## Exercise 2: Calculator

Write a program, `calculator.py` that asks for two numbers and an operator, and then prints the result of the operation.

Example:

```bash
$ python calculator.py
First number: 10
Second number: 5
Operator: +
Result: 15
```

## Arguments and argparse

So far, we have been using `input()` to get user input. This is fine for small programs, but what if we want to run our program from the terminal? We can do this by using arguments.

Arguments are values that we can pass to our program when we run it. For example, we can run our calculator program like this:

```bash
$ python calculator.py --first 10 --second 5 --operator +

Result: 15
```
Or for our hello program:

```bash
$ python hello.py --name Harry
```

We can do this by using the `argparse` module. This module allows us to define arguments for our program, and then parse them. Let us look at an example:

```py
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="The name of the person to greet")
    args = parser.parse_args()
    return args.name

def main():
    name = parse_args()
    print(f"Hello {name}!")


if __name__ == "__main__":
    main()
```

Which you can then call using:
```
$ python hello.py --name Harry
```
Which then prints
```
Hello Harry!
```


### Conceptual 1:
- Write a docstring for the `parse_args` function and add a type hint for the return value.
- Explain what the `if __name__ == "__main__":` does. Try running it in the debugging.

### Exercise 3: Calculator with argparse

Rewrite your calculator program to use argparse instead of `input()`. You should be able to run it like this:

```bash
$ python calculator_with_args.py --first 10 --second 5 --operator +
Result: 15
```



