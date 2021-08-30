import numpy as np

class network():
    """
    A network class for the neural network which include the following methods:
        
        - feedforward(), for using the network on a given input
        - SGD(), for apply Stochastic gradient descent (e.g. training the 
        network)
        - BP(), for apply backpropergation, this function is intented to be
        called using SGD()
        - cost(), for calculating the cost of a given input in regards to the
        desired output
        - eval(), for evaluation the performance of the network, while
        training
    """

    def __init__(self, l_sizes: list):
        """
        Where mu and sigma to adjust the initial starting parameters for the
        neural network (w, b is weight and bias, respectively)
        Note l_sizes (layer sizes) is given as a list of layers sizes.
        Note that the first layers does not contain weights and biases.

        Note that there is good argument for initializing the biases at zero
        following the Stanford CS231N Notes:
        http://cs231n.github.io/neural-networks-2/
        (not mentioned in the assigment, its effects is not (yet) explored)
        """
        self.n_layers = len(l_sizes)
        self.layer_sizes = l_sizes

        # Setting random biases using by default N(0, 1) (intercepts)
        self.biases = [np.sqrt(b_sigma)*np.random.randn(x, 1)
                      for x in l_sizes[1:]]

        # Setting random weights using by default N(0, 1) (beta values)
        self.weights = [np.sqrt(w_sigma)*np.random.randn(y, x) + w_mu
                        for x, y in np.array((l_sizes[:-1], l_sizes[1:])).T]

    def feedforward(self, x, save_var = False):
        """
        Returns prediction of the network given the input, x

        Assumes n_input is a np.array of shape (dimension) (n,) or (n, 1),
        where n is equal to size of the first layers (e.g. l_sizes[0])
        """

        # Used debugging and for backpropergations (BP)
        if save_var == True:
            xs = x
            l_activation = [x]  # a list of all the layer activation (with sigmoid)
            x_list = []  # list of vectors, one for each layer (without sigmoid)
            
            # Note that the calc is split up as to save variables underway
            for l in range(self.n_layers-1):
                x = np.dot(self.weights[l], xs) + self.biases[l]  
                x_list.append(x)
                xs = sigmoid(x)
                l_activation.append(xs)
            return x_list, xs, l_activation

        # Tranforming input in case of dim (n,), it does not influence (n, 1)
        x = x.reshape(-1, 1)

        # Note this could be optimized using matrix multiplication
        # -1 since x is the input layer
        for l in range(self.n_layers-1):
            x = sigmoid(np.dot(self.weights[l], x) + self.biases[l])
        return x

    def SGD(self, train_data, epochs, batch_size, learning_rate,
            test_data=None, save_performance = False):
        """
        Stochastic Gradient Descent (SGD)

        Loops through the number of epochs, splitting to training data into
        evenly sized chunk of size n, where n is the batch size. Then loops
        over each of these and applying Backpropergation (BP).
        
        Lastly if a test data is given it evaluates the network performance on
        the testdata using the eval() function
        """
        
        # Copying the data in as to not reorder the original data, 
        # keeping the same name for readability. 
        train_data = train_data[:]

        # Save a list for performance to be saved in
        if save_performance:
            if not test_data:
                raise Exception("Performance can't be saved if no test data is given")
            self.performance = []

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
                self.BP(batch, learning_rate)

            if test_data:
                n_correct, n = self.eval(test_data)
                print(f", Obtained Accuracy: {np.round(n_correct/n, 2)}" + 
                                              f" \t ({n_correct}/{n})", end="")
            if save_performance:
                n_correct_train, n_t = self.eval(train_data, train_data = True)
                self.performance.append((n_correct/n, n_correct_train/n_t))

        print("\n Process complete")

    def BP(self, batch, learning_rate):
        """
        Backpropergation (BP)

        loops trough each training sample in the batch and applies gradient
        descent. Lastly it averages the gradient vector and updates the wieghts
        and biases of the network.

        Where a batch is a tuple of length 2 on the form (pixels, answer).
        Where pixels is a list of pixel activation (zero is black) and answer
        is a boolean list og length 10, indicating the number of the digit.
        (assumes the MNIST data)
        
        """
        n_biases = [np.zeros(bias.shape) for bias in self.biases]
        n_weights = [np.zeros(weight.shape) for weight in self.weights]

        # looping over each batch, applying gradient descent
        for pixels, answer in batch:
            ### start BP
            dn_biases = [np.zeros(b.shape) for b in self.biases]
            dn_weights = [np.zeros(w.shape) for w in self.weights]
            
            # feedforward - where we save relevant variables
            x_list, activation, activations = self.feedforward(pixels, save_var=True)

            # update the weight and biases going backward in the N.N.
            delta = self.cost(activations[-1],
                              answer) * sigmoid(x_list[-1],  derivative=True)

            dn_biases[-1] = delta
            dn_weights[-1] = np.dot(delta, activations[-2].transpose())

            # Note that the following loop is loop backwards
            for l in range(2, self.n_layers):
                x = x_list[-l]
                s_deriv = sigmoid(x, derivative=True)
                delta = s_deriv * np.dot(self.weights[-l+1].T, delta)
                
                # Saving dn's
                dn_biases[-l] = delta
                dn_weights[-l] = np.dot(delta, activations[-l-1].T)



            for l in range(self.n_layers-1):
                n_biases[l] += dn_biases[l]
                n_weights[l] += dn_weights[l]

        # update weight and biases - averaged and weighted by the learning rate
        for l in range(self.n_layers-1):
            self.weights[l] = self.weights[l] - (learning_rate / len(batch)) * n_weights[l]
            self.biases[l] = self.biases[l] - (learning_rate / len(batch)) * n_biases[l]

    def cost(self, output, actual, derivative = True):
        """
        A cost function, which returns the difference between the output of the
        neural network (e.g. its prediction) and the actual value

        Note that this is (in part, se note of the end) a partial derivative of
        the cost function given by (in laTeX):
        \frac { 1 }{ 2 } \sum _{ n }{ \frac { |f(x)-a|^{ 2 } }{ 2 }  }
        where n is the number of observations, f(x) is the output of the neural
        network and a is the actual result.
        """
        
        # In practice only the derived function is used, consequently the 
        # original function serves only a conceptual purpose
        if derivative == False:
            return 1/2 * (output - actual)*(output - actual)
        
        return(output - actual)

    def eval(self, data, train_data = False):
        """
        Evaluates the network on a given test data, returning a tuple with
        the number of correct predictions and the total number of predicitons.
        assumes the MNIST database or data with similar structure
        """
        # creates a 2 by n matrix, where n is the length of the test_data
        # where the second column indicates the right answer
        # Note that there is a restructering for the train_data due to the
        # different structures of train and test_data
        if train_data:
            predictions = np.array([(np.argmax(self.feedforward(pixels)), np.argmax(answer))
                                    for pixels, answer in data])
        else:
            predictions = np.array([(np.argmax(self.feedforward(pixels)), answer)
                                    for pixels, answer in data])
                                
        n_correct = sum(predictions[:, 0] == predictions[:, 1])
            
        return (n_correct, len(predictions))
