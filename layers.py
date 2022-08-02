import numpy as np

class Dense:
    def __init__(self, n_inputs, n_neurons, activation):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        self.activation = activation
    def forward(self, inputs):
        output = np.dot(inputs, self.weights) + self.biases
        self.output = self.activation.forward(output)