
# Prerequisites
---

The introduction to basic linear algebra including
> matrix multiplication
> task: minimizing a parabola
> task: sigmoid

Let us first briefly introduce a neural network. Simple case logistic regression.

> draw a neural network
> show the calculations
> show that it is equal to matrix multiplication (+ bias)

So given this you should be able to implement the forward pass. For the weights and biases simply sample them from a normal distribution.

> Task 1

This is naturally a stupid network. It can't do anything. We want it to learn. For this we need a cost function. We will simply use the mean squared error:

$$
cost(x, y) : = \frac{1}{n} \sum_x (y - f(x))^2
$$

Following what we did in the exercise yesterday it is easy to see that we can diffentiate this 
$$
cost(x, y) : = \frac{1}{n}  \sum_x (y - f(x))^2
$$



Exercises
Task 1: Create a class called `Network`. The network should generate weight and biases and have a method `forward()` which takes in a vector of 10 values and perform the forward pass returning a single value.

**Bonus**: Generalize the function to take in `n` input values

**Bonus**: Generalize the function to output in `n` output values

**Bonus**: Generalize the function to have multiple layers as defined by a list e.g. the first network would be `[10, 1]`

Task 2:



# Learning more
---
>  3b1b tutorial

> michael nielsens book