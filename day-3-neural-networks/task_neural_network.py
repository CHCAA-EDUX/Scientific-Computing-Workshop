"""
Fully connected feedforward neural network
"""
from typing import List, Tuple

import numpy as np
import mnist_loader


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

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Performs the feedforward pass of the neural network.

        Args:
            X (np.ndarray): The input array. Assumes the shape of the input is (n,) or (n, 1),
        where n is equal to size of the first layers. For the MNIST data this will be pixels.

        Returns:
            np.ndarray: The prediction of the neural network
        """

        # for each layer in the network
            # (dot) multiply by the weights
            # add the bias
            # apply the activation function
        
        # feel free to do this as a for loop if you wish to begin with.
        pass

    # static methods simply mean that it does not take in self as an argument,
    # thus have not access to the class it is essentially just a function attached to the class
    @staticmethod
    def cost(
        output: np.ndarray,
        actual: np.ndarray,
    ) -> float:
        """A cost function, which returns the difference between the output of the
        neural network (e.g. its prediction) and the actual value

        The cost function given by
        sum((f(x) - a)^2) / n

        where n is the number of observations, f(x) is the output of the neural
        network and a is the actual result. The thing within the sum the the
        mean squared error.

        Args:
            output (np.ndarray): the output of the network
            actual (np.ndarray): the actual result
        Returns:
            np.ndarray: The loss/cost
        """
        pass

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
        over each of these and applying backpropergation.

        It can also include a validation data where it applies the evaluate function
        every epoch and prints the print.

        Args:
            train_datq (list): a list of training samples
            learning_rate (float): the learning rate. Lowering it will make the network
                learn slower (but finding better minimums). raising it will have the
                network learn faster. A good place to start it 3.
            epochs (int): Number of repetitions of the SGD.
            batch_size (int): Size of the batches used.
        """
        
        # for each epochs (epochs just mean number of repeats)
            # (print epoch)
            # shuffle the data (hint: there is a package called random)
            # create batches of data
            # backprop the given batch
            # (optional: print performance on validation)
        pass

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
        # for each sample in data
            # do a forward pass
            # compare the output with the answer
        # return number of correct and total number of predictions.
        pass


if __name__ == "__main__":

    # Setting a random seed for exercise consistency
    np.random.seed(seed=1337)

    train_data, val_data, test_data = mnist_loader.load_data_wrapper()

    ## init your neural network
    # network = NeuralNetwork([784, 30, 10])

    ## test forward pass on one example
    # pixels = train_data[0][0] # one example
    # answer = train_data[0][1]
    # output = network.forward(X=pixels)

    ## calculate the cost
    # cost = network.cost(output, actual=answer)

    ## train using backprop.
    ## (this should be very slow with stachostic gradient descent)
    # for i in range(10):
    #     network.backprop(train_data, learning_rate=3)
    #     print(network.evaluate(val_data))

    ## train for one epoch
    # network.SGD(train_data=train_data, epochs=1)
    
    ## evaluate the performance:
    # print(network.evaluate(val_data))