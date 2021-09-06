
## Introduction to Neural Networks

### Prerequisites

The introduction to basic linear algebra (day 2) including
- matrix multiplication
- task: minimizing a parabola
- task: sigmoid

## Plan

---

### What is a neural network?

This section starts with an explanation of the neuron, followed by an abstraction of the concept into notation followed by its vector form.


### The data
This section introduces the MNIST data. Then it goes on to introduce what use of representation we might expect the neural network to learn, using Hubel and Weisel experiment as an example. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/IOHayh06LJ4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Lastly, the student will implement the feedforward of the neural network and get the first look at the scripts.

### Getting it to learn
This section will define the cost function. Then it will go on to starting with a naïve approach about how one might train the neural network, before explaining backpropagation along with stochastic gradient descent.

After a break here we will briefly go through the backpropagation script. Then we talk about stochastic gradient descent (SGD).

### How to tackle the exercise

Introduction and walkthrough of the exercises. We will start of with getting the whole thing up and running before we start experimenting more with it.

After that. First of all congratulations on implementing a neural network is in order. Then there is the following tasks (feel free to take them in order of interest):

- Generate a sample of random noise.
  - What does the model predict? Is it sure about its prediction?
- Improve the performance of the neural network
   - What changing the number of hidden layers change anything?
   - What does adjusting the learning rate do? 
   - What about the batch size?
- plot the loss over epoch both on the test and the train set. When should you stop training?
- replace the sigmoid function with a relu activation function 
- Challenging: Visualize the weight matrices (something like a heatmap where positive values are 'warm' and negative values are 'cold')
  - What do the visualizations reveal?


## Learning more
---

This is just the start of neural networks. To learn more I recommend [the videos](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) by 3blue1brown and the [book](http://neuralnetworksanddeeplearning.com/index.html) by Michael Nielsen.

### Next time teaching this section
- [ ] Add justification on why learning neural networks is relevant
- [ ] edit code
  - [ ] fix backprop such that shape of the weight and biases doe not matter (transpose if [784, 30] instead of [30, 784], where 30 is the first hidden layer)
  - [ ] similarly or reshape bias to (30, 1) if it is (30,)
  - [ ] remove dependency on the number of layers and extrapolate these from the number of bias matrices.
