"""
Fully connected feedforward neural network
"""
from typing import List, Tuple

import numpy as np
import mnist_loader

import random


def sigmoid(x: np.ndarray, derivative: bool = False) -> np.ndarray:
    """
    The sigmoid function which is given by
    1/(1+exp(-x))

    Where x is a number or np vector. if derivative is True it applied the
    derivative of the sigmoid function instead.

    Examples:
    >>> sigmoid(0)
    0.5
    >>> abs(sigmoid(np.array([100, 30, 10])) - 1) < 0.001
    array([ True,  True,  True])
    >>> abs(sigmoid(-100) - 0) < 0.001
    True
    """
    if derivative:
        return sigmoid(x) * (1 - sigmoid(x))
    return 1 / (1 + np.exp(-x))


def chunks(l, n):
    """
    Creating a iterator which yield successive n-sized chunks from the list, l.

    This function is heavily inspired by the following blogpost:
    https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

    Examples:
    >>> L = [(1,2), (1,2), (1,2), (3,3), (3,3), (3,3), (3,3)]
    >>> output = chunks(L, 2)
    >>> max([len(x) for x in output])
    2
    """
    try:
        assert float(n) % 1 == 0, "n is not a whole number"
    except ValueError:
        "Make sure n is a whole number"
    assert isinstance(l, list), "Make sure that l is a list"

    for i in range(0, len(l), n):
        yield l[i : (i + n)]


class NeuralNetwork:
    def __init__(self, layers: List[int]):
        """initializes the neural network by creating a weight matrice pr. layer and a bias pr. layer.
        The bias and wieght are randomly sampled from a Normal(0, 1).

        Args:
            layers (List[int]): A list of layers. Where the integers denote the number of nodes in the layer.
                The first layer is the input layer and should for MNIST always be 784 (corresponding to n. pixels).
                While the last layer should contain 10 nodes. Corresponding to the number of output classes. Example input:
                [784, 30, 10]
        """
        ## init biases
        # self.biases = ...
        ## init list of weight matrices
        # self.weights = ...

        self.n_layers = len(layers)
        self.layer_sizes = layers

        # Setting random biases using by default N(0, 1) (intercepts)
        self.biases = [np.random.randn(x, 1) for x in layers[1:]]

        # Setting random weights using by default N(0, 1) (beta values)
        self.weights = [
            np.random.randn(y, x) for x, y in np.array((layers[:-1], layers[1:])).T
        ]

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Performs the feedforward pass of the neural network.

        Args:
            X (np.ndarray): The input array. Assumes the shape of the input is (n,) or (n, 1),
        where n is equal to size of the first layers.

        Returns:
            np.ndarray: The prediction of the neural network
        """
        # Tranforming input in case of dim (n,), it does not influence (n, 1)
        x = X.reshape((-1, 1))

        # Note this could be optimized using matrix multiplication
        # -1 since x is the input layer
        for l in range(self.n_layers - 1):
            x = sigmoid(np.dot(self.weights[l], x) + self.biases[l])
        return x

    # static methods simply mean that it does not take in self as an argument,
    # thus have not access to the class it is essentially just a function attached to the class
    @staticmethod
    def cost(
        output: np.ndarray,
        actual: np.ndarray,
    ) -> np.ndarray:
        """A cost function, which returns the difference between the output of the
        neural network (e.g. its prediction) and the actual value

        The cost function given by
        1/2 * (f(x) -a)^2

        where n is the number of observations, f(x) is the output of the neural
        network and a is the actual result.

        Args:
            output (np.ndarray): the output of the network
            actual (np.ndarray): the actual result
        Returns:
            np.ndarray: The loss/cost
        """
        return sum(output - actual) / len(actual)

    def SGD(
        self,
        train_data: list,
        learning_rate: float,
        epochs: int = 1,
        batch_size: int = 10,
    ) -> None:
        """
        Stochastic Gradient Descent (SGD)

        Loops through the number of epochs, splitting to training data into
        evenly sized chunk of size n, where n is the batch size. Then loops
        over each of these and applying Backpropergation (BP).

        Lastly if a test data is given it evaluates the network performance on
        the testdata using the eval() function
        """
        
        # for each epochs (epochs just mean number of repeats)
            # shuffle the data
            # create batches of data
            # backprop the given batch


        # Copying the data in as to not reorder the original data,
        # keeping the same name for readability.
        train_data = train_data[:]

        for epoch in range(epochs):
            print(f"\n Epoch: {(epoch+1)}/{epochs}", end="")
            random.shuffle(train_data)  # Using a Fisher Yates Shuffle

            batches = chunks(train_data, batch_size)

            # Note that instead of looping through each batch, you could have
            # a more effective approach would be to consider each batch as a
            # vector in a matrix, and from here simply use matrix
            # multiplication
            for batch in batches:
                # Apply backpergation using gradient descent for each batch
                self.backprop(batch, learning_rate)
            print()

        print("\n Process complete")

    def backprop(self, batch, learning_rate: float) -> None:
        """
        loops trough each training sample in the batch and applies gradient
        descent. Lastly it averages the gradient vector and updates the weights
        and biases of the network.

        Where a batch is a tuple of length 2 on the form (pixels, answer).
        Where pixels is a list of pixel activation (zero is black) and answer
        is a boolean list og length 10, indicating the number of the digit.
        """
        n_biases = [np.zeros(bias.shape) for bias in self.biases]
        n_weights = [np.zeros(weight.shape) for weight in self.weights]

        # looping over each batch, applying gradient descent
        for pixels, answer in batch:
            ### start BP
            dn_biases = [np.zeros(b.shape) for b in self.biases]
            dn_weights = [np.zeros(w.shape) for w in self.weights]

            ### feedforward - where we save relevant variables
            x = pixels
            activations = [pixels]  # a list of all the layer activation (with sigmoid)
            zs = []  # list of activations, one for each layer (without sigmoid)

            # Note that the calc is split up as to save variables underway
            for l in range(self.n_layers - 1):
                x = np.dot(self.weights[l], x) + self.biases[l]
                zs.append(x)
                x = sigmoid(x)
                activations.append(x)

            # update the weight and biases going backward in the N.N.
            delta = (activations[-1] - answer) * sigmoid(  # derivative of cost
                zs[-1], derivative=True
            )

            dn_biases[-1] = delta
            dn_weights[-1] = np.dot(delta, activations[-2].transpose())

            # Note that the following loop is loop backwards
            for l in range(2, self.n_layers):
                x = zs[-l]
                s_deriv = sigmoid(x, derivative=True)
                delta = s_deriv * np.dot(self.weights[-l + 1].T, delta)

                # Saving dn's
                dn_biases[-l] = delta
                dn_weights[-l] = np.dot(delta, activations[-l - 1].T)

            for l in range(self.n_layers - 1):
                n_biases[l] += dn_biases[l]
                n_weights[l] += dn_weights[l]

        # update weight and biases - averaged and weighted by the learning rate
        for l in range(self.n_layers - 1):
            self.weights[l] = (
                self.weights[l] - (learning_rate / len(batch)) * n_weights[l]
            )
            self.biases[l] = self.biases[l] - (learning_rate / len(batch)) * n_biases[l]

    def evaluate(self, data: list) -> Tuple[int, int]:
        """Evaluates the network on a given test data, returning a tuple with
        the number of correct predictions and the total number of predicitons.

        Args:
            data (list): A list of tuples of size 2, where the first element is the input
                for MNIST this is pixels and the second element is the correct answer
                (e.g. what digit it is) response.

        Returns:
            Tuple[int, int]: A tuple where the first entry it the number of correct and the second entry
                is the total number of predictions.
        """
        # creates a 2 by n matrix, where n is the length of the test_data
        # where the second column indicates the right answer
        # Note that there is a restructering for the train_data due to the
        # different structures of train and test_data
        predictions = np.array(
            [(np.argmax(self.forward(pixels)), answer) for pixels, answer in data]
        )

        n_correct = sum(predictions[:, 0] == predictions[:, 1])

        return (n_correct, len(predictions))


if __name__ == "__main__":

    # Setting a random seed for exercise consistency
    np.random.seed(seed=1337)

    train_data, val_data, test_data = mnist_loader.load_data_wrapper()

    ## init your neural network
    # network = NeuralNetwork(...)
    network = NeuralNetwork([784, 30, 10])

    ## test forward pass on one example
    # pixels = train_data[0][0] # one example
    # answer = train_data[0][1]
    # output = network.forward(X=pixels)
    pixels = train_data[0][0]  # one example
    answer = train_data[0][1]
    output = network.forward(X=pixels)

    ## calculate the cost
    # cost = network.cost(output, actual=answer)
    cost = network.cost(output, actual=answer)

    ## train using backprop.
    ## (this should be very slow with stachostic gradient descent)
    # for i in range(10):
    #     network.backprop(train_data, learning_rate=3)
    #     print(network.evaluate(val_data))

    ## train for one epoch
    # network.SGD(train_data=train_data, epochs=1)
    network.SGD(train_data=train_data, epochs=1)
    
    ## evaluate the performance:
    # print(network.evaluate(val_data))
