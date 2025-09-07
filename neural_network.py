"""
A module to build a neural network from scratch with NumPy.
This is a teaching tool to illustrate the principles of backpropagation.

For a full, step-by-step explanation of this code and the concepts
behind it, please read the accompanying README.md file.
"""

import numpy as np


# The activation function and its derivative.
# We'll use the sigmoid function, a classic choice.
def sigmoid(x):
    """Squashes the input to be between 0 and 1."""
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    """The gradient of the sigmoid function."""
    return x * (1 - x)


class Layer:
    """
    A Layer is a "Council of Elders" in our network.
    It's a collection of neurons that processes signals as a single, unified entity.
    It holds a weight matrix (the council's wisdom) and a bias vector (their inclinations).
    """

    def __init__(self, num_inputs, num_neurons):
        # We initialize weights with small random numbers.
        self.weights = np.random.randn(num_inputs, num_neurons) * 0.1
        self.biases = np.zeros((1, num_neurons))
        self.inputs = None
        self.output = None

    def forward(self, inputs):
        """
        Passes the inputs through the entire layer at once.
        """
        self.inputs = inputs
        total_signal = np.dot(inputs, self.weights) + self.biases
        self.output = sigmoid(total_signal)
        return self.output


class NeuralNetwork:
    """
    The Neural Network is the full "Temple" that houses the layers.
    It orchestrates the flow of information forward and the whispers of learning backward.
    """

    def __init__(self, layer_sizes):
        # layer_sizes is a list like [num_inputs, num_hidden_neurons, num_outputs]
        # e.g., [2, 3, 1] for a network with 2 inputs, 1 hidden layer of 3 neurons, and 1 output neuron.
        self.layers = []
        for i in range(len(layer_sizes) - 1):
            num_inputs = layer_sizes[i]
            num_neurons = layer_sizes[i + 1]
            self.layers.append(Layer(num_inputs, num_neurons))

    def forward(self, inputs):
        """
        The full "thought" process, or the Forward Pass.
        Passes the input through all layers of the temple.
        """
        current_inputs = inputs
        for layer in self.layers:
            current_inputs = layer.forward(current_inputs)

        # The final output of the last layer is the network's prediction.
        return current_inputs

    def train(self, X_train, y_train, epochs, learning_rate):
        """
        The "Training Dojo." This is where the network practices and learns.
        """
        for epoch in range(epochs):
            total_error = 0
            for x, y_true in zip(X_train, y_train):
                # 1. Predict (Forward pass)
                # Reshape x to be a 2D array for dot product
                x = x.reshape(1, -1)
                y_pred = self.forward(x)

                # 2. Calculate Error (Listen to the grumpy droid)
                total_error += mse(y_true, y_pred)

                # 3. Learn (The whispers of blame)
                self.backward(y_true, y_pred, learning_rate)

            # Print the progress, so we can watch it learn
            if (epoch + 1) % 100 == 0:
                avg_error = total_error / len(X_train)
                print(f"Epoch {epoch + 1}/{epochs}, Error: {avg_error:.6f}")

    def backward(self, y_true, y_pred, learning_rate):
        """
        This is the sacred art: Backpropagation.
        It sends the "whispers of blame" backward through the network.
        """
        # Start with the error from the grumpy droid
        error = mse_derivative(y_true, y_pred)

        for layer in reversed(self.layers):
            # The "blame" for this layer is the incoming error times the derivative of its activation
            delta = error * sigmoid_derivative(layer.output)

            # Calculate the gradient of the weights and biases
            d_weights = np.dot(layer.inputs.T, delta)
            d_biases = np.sum(delta, axis=0, keepdims=True)

            # Update the weights and biases
            layer.weights -= learning_rate * d_weights
            layer.biases -= learning_rate * d_biases

            # Pass the error "whisper" to the previous layer
            error = np.dot(delta, layer.weights.T)


# --- Training Utilities ---


def mse(y_true, y_pred):
    """
    Mean Squared Error: our "Grumpy Droid" loss function.
    It measures how wrong the network's predictions are.
    """
    return np.mean(np.power(y_true - y_pred, 2))


def mse_derivative(y_true, y_pred):
    """The derivative of the MSE loss function."""
    return 2 * (y_pred - y_true) / y_pred.size


if __name__ == "__main__":
    # --- The Awakening ---
    # We will teach our network the XOR function, its final test.
    # This is a classic problem that requires a hidden layer.

    # 1. The training data (The XOR Puzzle)
    X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_train = np.array([[0], [1], [1], [0]])

    # 2. The network architecture (The Temple's design)
    # 2 inputs -> 3 neurons in a hidden layer -> 1 output neuron
    network = NeuralNetwork([2, 3, 1])

    # 3. The training regimen (The Dojo's schedule)
    epochs = 10000
    learning_rate = 0.1

    print("Beginning the training ritual...")
    network.train(X_train, y_train, epochs, learning_rate)
    print("The network has completed its training.")

    # 4. The test of wisdom (The final exam)
    print("\nLet's see the wisdom it has gained:")
    for x, y_true in zip(X_train, y_train):
        prediction = network.forward(x.reshape(1, -1))
        print(f"Input: {x}, Prediction: {prediction[0][0]:.4f}, Actual: {y_true[0]}")
