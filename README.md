# The Path of the Python Padawan: Demystifying Backpropagation

Welcome, young apprentice, to the AI-dojo. You have been chosen to embark on a sacred journey: building a neural network from scratch. Many believe this art is shrouded in the dark magic of calculus, but we shall reveal its true nature. It is not magic, but the Force of logic, a flow of information that you can build and command with your own hands using Python and NumPy.

This repository contains a single Python scroll, `neural_network.py`, which holds the complete blueprint for a thinking machine. This document, your holocron, will be your guide. We will walk through the code step-by-step, not just explaining _what_ it does, but _why_ it does it, and how each piece connects to the grand design.

Our quest is to build a network that can learn the classic XOR problem, a task that requires a true "hidden layer" of understanding.

## A Worthy Challenge: The Tale of XOR

Before we forge our first component, every Padawan must understand the challenge that awaits. Our network's final exam will be to solve the puzzle of **XOR (Exclusive OR)**.

What is XOR? It is a simple, fundamental rule of logic:

- If two inputs are the **same** (both `0` or both `1`), the output is `0`.
- If two inputs are **different** (one `0` and one `1`), the output is `1`.

You could draw it on a datapad like this:

| Input 1 | Input 2 | Output |
| :-----: | :-----: | :----: |
|    0    |    0    | **0**  |
|    0    |    1    | **1**  |
|    1    |    0    | **1**  |
|    1    |    1    | **0**  |

This puzzle may seem simple, but it holds a legendary place in the history of AI. In the early days, the first and simplest neural networks, called Perceptrons, were unable to solve it. They could only learn patterns that could be separated by a single straight line. If you plot the XOR points, you will see that you cannot separate the `0`s from the `1`s with just one line.

This failure led to a "dark age" for AI research. The solution required a network with an extra "hidden layer" of neurons—a layer of deeper understanding. By teaching our network to solve XOR, we are not just solving a puzzle; we are recreating one of the great breakthroughs in the journey toward true artificial intelligence. This is the mountain we must climb.

## The Journey Ahead

Our training is divided into four parts:

1.  **Part 1: Assembling the Thinking Machine**: We will forge the components of our network's mind—the Layers and the Network itself.
2.  **Part 2: The Art of Learning**: We will bestow upon our creation the ability to learn from its mistakes using a Loss Function and the fabled art of Backpropagation.
3.  **Part 3: The Training Dojo**: We will create the training loop where our network will practice and grow wise.
4.  **Part 4: The Awakening**: We will put our network to the test and witness it solve the XOR puzzle.

Prepare yourself. The path to enlightenment begins now.

---

## Part 1: Assembling the Thinking Machine

A mind, whether biological or artificial, is not a single entity. It is a collection of smaller, simpler parts working in concert. Our first task is to forge these fundamental components.

### The Council of Elders: The `Layer` Class

Initially, we considered building individual `Neuron` crystals. A neuron is the smallest unit of thought; it takes inputs, weighs their importance, and decides whether to send a signal.

However, a more powerful way to channel the Force is to think of a whole group of neurons working together as a single unit—a `Layer`. In our code, this is the `Layer` class.

```python
class Layer:
    def __init__(self, num_inputs, num_neurons):
        # A matrix of "wisdom"
        self.weights = np.random.randn(num_inputs, num_neurons) * 0.1
        # A vector of "inclinations"
        self.biases = np.zeros((1, num_neurons))
        # ...

    def forward(self, inputs):
        # ...
        total_signal = np.dot(inputs, self.weights) + self.biases
        self.output = sigmoid(total_signal)
        return self.output
```

- **`weights`**: This is a matrix. Think of it as the collected wisdom of the entire layer. Each column represents a single neuron, and each value in that column is the importance (the "weight") that neuron assigns to one of the incoming signals.
- **`biases`**: This is a vector. Each neuron has a bias, which is its own personal "inclination" to activate, even before considering any inputs. It helps the network make decisions that aren't purely based on the input signals.
- **`forward(inputs)`**: This is the "thinking" process of the layer. It takes the `inputs`, performs a matrix multiplication with the `weights`, adds the `biases`, and then passes the result through an `activation function` (we use `sigmoid`) to produce the layer's output.

### The Temple: The `NeuralNetwork` Class

A single layer can learn simple patterns. But to learn complex ideas, we must stack these layers one after the other, forming a deep network. The `NeuralNetwork` class is the temple that houses these layers.

````python
class NeuralNetwork:
    def __init__(self, layer_sizes):
        self.layers = []
        for i in range(len(layer_sizes) - 1):
            # ... create Layers ...

    def forward(self, inputs):
        current_inputs = inputs
        for layer in self.layers:
            current_inputs = layer.forward(current_inputs)
        return current_inputs
-   The `forward` method here orchestrates the entire flow of thought. It takes the initial input and passes it through the first layer. The output of that layer then becomes the input for the second layer, and so on, until a final prediction emerges from the last layer. This is the **Forward Pass**.

---

## Part 2: The Art of Learning

Our network can think, but it cannot learn. It is a mind without a teacher, speaking random words. To gain wisdom, it must be able to recognize its own mistakes and correct them.

### The Grumpy Droid: The Loss Function

Before the network can learn, it needs a way to measure how wrong its predictions are. This is the job of the **Loss Function**.

We use the Mean Squared Error (MSE), which you can imagine as a grumpy training droid.

```python
def mse(y_true, y_pred):
    return np.mean(np.power(y_true - y_pred, 2))
````

It takes the correct answer (`y_true`) and the network's prediction (`y_pred`), finds the difference, and squares it. Squaring makes the error positive and punishes large errors more severely. The goal of all our training is to make this grumpy droid happy by getting the loss score as close to zero as possible.

### The Whispers of Blame: Backpropagation

This is the most sacred and misunderstood art. Once our grumpy droid yells out the error score, how do we use that information to fix the millions of weights and biases inside the network?

The answer is **Backpropagation**. It is the art of sending the error message _backward_ through the temple.

Imagine the final output neuron made a mistake. Backpropagation starts by telling this neuron how badly it was wrong. This neuron then looks at the signals it received from the layer before it and calculates, "How much did each of these signals contribute to my mistake?" It then "whispers" a share of the blame back to each of those neurons.

This process repeats, layer by layer. Each neuron receives a "blame score" (called a gradient), uses it to adjust its own weights and biases, and then passes a calculated share of the blame to the neurons in the layer before it.

```python
    def backward(self, y_true, y_pred, learning_rate):
        # Start with the error at the final layer
        error = mse_derivative(y_true, y_pred)

        for layer in reversed(self.layers):
            # Calculate this layer's contribution to the error
            delta = error * sigmoid_derivative(layer.output)

            # Calculate how much to change the weights and biases
            d_weights = np.dot(layer.inputs.T, delta)
            d_biases = np.sum(delta, axis=0, keepdims=True)

            # Update the weights and biases to reduce future error
            layer.weights -= learning_rate * d_weights
            layer.biases -= learning_rate * d_biases

            # Pass the error "whisper" to the previous layer
            error = np.dot(delta, layer.weights.T)
```

The "scary calculus" is simply the language of these whispers. The `mse_derivative` and `sigmoid_derivative` functions allow us to precisely calculate the blame for each neuron. The `learning_rate` is a small number that controls how drastically we change the weights—too high, and our learning is unstable; too low, and it's too slow.

---

## Part 3: The Training Dojo

We have a mind that can think and a method for it to learn. Now we need a place for it to practice. The `train` method is our dojo. It follows a simple, powerful rhythm that is the heartbeat of all machine learning.

```python
    def train(self, X_train, y_train, epochs, learning_rate):
        for epoch in range(epochs):
            for x, y_true in zip(X_train, y_train):
                # 1. Predict (Forward pass)
                y_pred = self.forward(x)

                # 2. Calculate Error (using the grumpy droid)
                # ...

                # 3. Learn (Backward pass / whispers of blame)
                self.backward(y_true, y_pred, learning_rate)
```

For a set number of rounds (called `epochs`), the network will:

1.  **Predict**: Look at an example from the training data and make a prediction (`forward`).
2.  **Measure Error**: Compare its prediction to the correct answer (`mse`).
3.  **Learn**: Adjust all its internal weights and biases based on the error (`backward`).
4.  **Repeat**: Do this over and over for all examples in the data, for many epochs.

With each cycle, the network's error gets smaller. It is learning.

---

## Part 4: The Awakening

The final step is to give our network a worthy challenge: the XOR problem. We instantiate the network, set the training parameters, and call our `train` method.

The output shows the network's journey. At first, its error is high. But after thousands of epochs of practice in the dojo, the error becomes very small.

```
Beginning the training ritual...
Epoch 100/10000, Error: 0.255476
...
Epoch 10000/10000, Error: 0.002102
The network has completed its training.
```

When we test its final wisdom, we see it has succeeded. It has learned to distinguish the complex pattern of XOR.

```
Let's see the wisdom it has gained:
Input: [0 0], Prediction: 0.0466, Actual: 0
Input: [0 1], Prediction: 0.9456, Actual: 1
Input: [1 0], Prediction: 0.9585, Actual: 1
Input: [1 1], Prediction: 0.0393, Actual: 0
```

Our creation is complete. It can think, learn, and solve problems.

---

## How to Run This Simulation

To begin your own training, follow these steps:

1.  **Install `uv`**: If you do not have it, `uv` is a fast and modern Python packaging tool. Follow the official instructions to install it.

2.  **Create the Virtual Environment**: Open your terminal in this repository and run:

    ```bash
    uv venv
    ```

    This creates a sacred, isolated space for our project.

3.  **Install Dependencies**: Install `numpy` into the environment:

    ```bash
    uv pip install numpy
    ```

4.  **Run the Scroll**: Execute the Python script using the interpreter from the virtual environment:
    ```bash
    .venv/bin/python neural_network.py
    ```

May the Force be with you on your journey to understanding.
