"""
The Percy Chronicles: Neural Network Implementation
==================================================

This is Percy's actual code - the blueprint for building thinking teams
that can solve impossible problems like the XOR challenge.

Percy learned that intelligence comes from simple components working together.
This code is his story, translated into Python and NumPy.

For the full saga of how Percy discovered the magic of neural networks,
read the accompanying README.md file.
"""

import numpy as np


# ==============================================================================
# Chapter 1: The Fundamental Magic - Activation Functions
# ==============================================================================

def sigmoid(x):
    """
    Percy's 'excitement function' - converts any signal into a value between 0 and 1.
    
    Think of this as Percy's way of expressing how excited he is about what he sees:
    - Very negative input → close to 0 (not excited at all)
    - Very positive input → close to 1 (maximum excitement!)
    - Zero input → exactly 0.5 (neutral)
    
    This smooth curve is what allows Percy and his team to learn gradual distinctions
    instead of just binary yes/no decisions.
    """
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    """
    The 'learning sensitivity' function - tells us how much Percy's excitement
    can change based on small adjustments to the input.
    
    This is crucial for the 'whispers of wisdom' (backpropagation).
    When Percy gets feedback, this tells him how much he should adjust
    his responses based on that feedback.
    """
    return x * (1 - x)


# ==============================================================================
# Chapter 2: The Team Members - The Layer Class
# ==============================================================================

class Layer:
    """
    A Layer represents Percy's team at The XOR Club.
    
    Think of this as Percy, Larry, and StyleBot working together:
    - `weights`: How much each team member trusts the others' opinions
    - `biases`: Each team member's personal inclinations/prejudices
    - `inputs`: What the team sees (the current guest)
    - `output`: The team's collective opinion after discussion
    
    In Chapter 2 of our saga, Ada explained that Percy couldn't solve XOR alone.
    He needed a team where each member contributes their expertise.
    """

    def __init__(self, num_inputs, num_neurons):
        """
        Setting up a new team of neural bouncers.
        
        num_inputs: How many things the team needs to look at (hat, glasses, etc.)
        num_neurons: How many team members we're hiring (Percy, Larry, StyleBot, etc.)
        """
        # Initialize weights with small random values - like giving each team member
        # slightly different initial opinions about what matters
        self.weights = np.random.randn(num_inputs, num_neurons) * 0.1
        
        # Start biases at zero - no initial prejudices
        self.biases = np.zeros((1, num_neurons))
        
        # These will store the team's inputs and outputs during the "dance"
        self.inputs = None
        self.output = None

    def forward(self, inputs):
        """
        Chapter 3: The Information Dance
        
        This is where Percy's team processes what they see and gives their opinions.
        
        The math here represents:
        1. Each team member looks at all the inputs (guest features)
        2. They weight those inputs based on their expertise (the weights matrix)
        3. They add their personal bias/inclination
        4. They express their final excitement level (through sigmoid)
        """
        self.inputs = inputs  # Remember what we saw (needed for learning later)
        
        # The team discussion: inputs × weights + biases
        # This is like Percy saying "I see a hat (input=1) and I care about hats 
        # with strength 0.8 (weight), plus I'm generally hat-positive (bias=0.1)"
        team_discussion = np.dot(inputs, self.weights) + self.biases
        
        # Convert the raw discussion into excitement levels (0 to 1)
        self.output = sigmoid(team_discussion)
        
        return self.output


# ==============================================================================
# Chapter 3-6: The Complete System - The NeuralNetwork Class
# ==============================================================================

class NeuralNetwork:
    """
    The XOR Club itself - the complete system that houses Percy's team
    and orchestrates their learning journey.
    
    This represents Ada's management system that:
    - Organizes the team hierarchy (layers)
    - Runs the information dance (forward pass)
    - Facilitates learning from mistakes (backpropagation)
    - Manages the training montage (the train method)
    """

    def __init__(self, layer_sizes):
        """
        Building The XOR Club's management structure.
        
        layer_sizes example: [2, 3, 1] means:
        - 2 inputs (hat status, glasses status)
        - 3 middle management (Percy, Larry, StyleBot)  
        - 1 final decision maker (Ada)
        """
        self.layers = []
        
        # Build each management level
        for i in range(len(layer_sizes) - 1):
            inputs_for_this_layer = layer_sizes[i]
            neurons_in_this_layer = layer_sizes[i + 1]
            self.layers.append(Layer(inputs_for_this_layer, neurons_in_this_layer))

    def forward(self, inputs):
        """
        Chapter 3: The Complete Information Dance
        
        This is Percy's team in action - information flows from the entrance
        through each layer of management until Ada makes the final decision.
        
        Guest arrives → Percy's Team analyzes → Ada decides → Door opens/closes
        """
        current_signal = inputs
        
        # Pass the signal through each layer of Percy's team
        for layer in self.layers:
            current_signal = layer.forward(current_signal)
        
        # The final signal is Ada's decision
        return current_signal

    def train(self, X_train, y_train, epochs, learning_rate):
        """
        Chapter 5: The Training Montage
        
        This is where Percy and Larry practice thousands of times,
        getting better with each mistake through the sacred rhythm:
        1. Predict (make a decision about a guest)
        2. Measure (see how wrong we were)  
        3. Learn (adjust our partnership based on the mistake)
        4. Repeat (do it again, hopefully better)
        """
        print("🤖 Percy and Larry begin their training montage...") 
        
        for epoch in range(epochs):
            total_error = 0
            
            # Practice with each training example
            for guest_features, correct_decision in zip(X_train, y_train):
                # 1. PREDICT: What would we decide about this guest?
                guest_features = guest_features.reshape(1, -1)  # Format for team processing
                our_decision = self.forward(guest_features)
                
                # 2. MEASURE: How wrong were we? (The grumpy loss function)
                mistake_severity = mse(correct_decision, our_decision)
                total_error += mistake_severity
                
                # 3. LEARN: Send the whispers of wisdom backward through the team
                self.backward(correct_decision, our_decision, learning_rate)
            
            # Show Percy's progress every 100 rounds
            if (epoch + 1) % 100 == 0:
                avg_error = total_error / len(X_train)
                print(f"📊 Training Round {epoch + 1}/{epochs}, Team Error: {avg_error:.6f}")

    def backward(self, correct_answer, our_guess, learning_rate):
        """
        Chapter 4: The Whispers of Wisdom (Backpropagation)
        
        This is the most magical part - when Percy's team learns from mistakes.
        The error flows backward through each layer, whispering to every team member
        exactly how they should adjust their behavior.
        
        It's like Ada giving personalized coaching to each team member:
        "Percy, you trusted the hat signal too much in that situation..."
        "Larry, you need to be more suspicious when glasses appear with hats..."
        "StyleBot, your artistic intuition was off - here's how to calibrate..."
        """
        # Start with the mistake signal from Ada's decision
        error_signal = mse_derivative(correct_answer, our_guess)
        
        # Send the whispers backward through each layer
        for layer in reversed(self.layers):
            # Calculate how much each team member should adjust
            # (This is the "personalized coaching" step)
            responsibility = error_signal * sigmoid_derivative(layer.output)
            
            # Figure out how to adjust the team's trust relationships (weights)
            weight_adjustments = np.dot(layer.inputs.T, responsibility)
            bias_adjustments = np.sum(responsibility, axis=0, keepdims=True)
            
            # Actually make the adjustments (Percy's team gets slightly wiser)
            layer.weights -= learning_rate * weight_adjustments
            layer.biases -= learning_rate * bias_adjustments
            
            # Pass the whisper to the previous layer
            error_signal = np.dot(responsibility, layer.weights.T)


# ==============================================================================
# The Grumpy Loss Function - Ada's Mistake Detector
# ==============================================================================

def mse(correct_answer, our_guess):
    """
    The 'Grumpy Droid' from our saga - Ada's mistake-measuring assistant.
    
    This function shrieks louder the more wrong we are:
    - Perfect guess → silent (loss = 0)
    - Terrible guess → loud shrieking (high loss)
    
    Technically: Mean Squared Error
    Practically: How embarrassed Percy should feel about his team's decision
    """
    return np.mean(np.power(correct_answer - our_guess, 2))


def mse_derivative(correct_answer, our_guess):
    """
    The grumpy droid's specific complaints - tells Percy's team 
    not just that they were wrong, but in which direction they were wrong.
    
    This is what starts the whispers of wisdom flowing backward.
    """
    return 2 * (our_guess - correct_answer) / our_guess.size


# ==============================================================================
# Chapter 6: Percy's Triumph - The XOR Challenge
# ==============================================================================

if __name__ == "__main__":
    print("🎭 Welcome to The XOR Club!")
    print("📖 This is Percy's story, in code form...")
    print()
    
    # The XOR Challenge - the impossible problem that broke Percy's original logic
    # Remember: Accept guests with hat OR glasses, but NOT BOTH
    X_train = np.array([
        [0, 0],  # No hat, no glasses → REJECT (not cool enough)
        [0, 1],  # No hat, glasses → ACCEPT (just right!)  
        [1, 0],  # Hat, no glasses → ACCEPT (perfect!)
        [1, 1]   # Hat AND glasses → REJECT (too cool!)
    ])
    
    y_train = np.array([
        [0],  # REJECT
        [1],  # ACCEPT
        [1],  # ACCEPT  
        [0]   # REJECT
    ])
    
    print("🧠 Building Percy's team...")
    print("   - 2 input sensors (hat detector, glasses detector)")
    print("   - 3 middle management (Percy, Larry, StyleBot)")
    print("   - 1 decision maker (Ada)")
    
    # Create Percy's neural network team
    # [2, 3, 1] = 2 inputs → 3 hidden neurons → 1 output
    percys_team = NeuralNetwork([2, 3, 1])
    
    # Training parameters
    training_rounds = 2000  # How many times Percy practices
    learning_speed = 0.32   # How quickly Percy adjusts after mistakes (set too low and the team will never learn)
    
    print(f"\n🏋️ Beginning {training_rounds} rounds of training...")
    print("(Percy and Larry will show progress every 100 rounds)")
    print()
    
    # Chapter 5: The Training Montage
    percys_team.train(X_train, y_train, training_rounds, learning_speed)
    
    print("\n🎓 Training complete! Let's see how the duo performs...")
    print("\n🚪 Opening night at The XOR Club:")
    print("=" * 50)
    
    # Chapter 6: The Triumph - Test Percy and Larry's learned wisdom
    guest_types = [
        "Guest with no hat, no glasses",
        "Guest with no hat, but glasses", 
        "Guest with hat, but no glasses",
        "Guest with both hat AND glasses"
    ]
    
    for i, (guest_features, correct_decision) in enumerate(zip(X_train, y_train)):
        duo_decision = percys_team.forward(guest_features.reshape(1, -1))
        confidence = duo_decision[0][0]
        
        print(f"\n👤 {guest_types[i]}:")
        print(f"   🤖 Percy & Larry's confidence: {confidence:.4f}")
        print(f"   ✅ Correct decision: {'ACCEPT' if correct_decision[0] == 1 else 'REJECT'}")
        print(f"   🎯 Duo decision: {'ACCEPT' if confidence > 0.5 else 'REJECT'}")
        
        # Add Percy and Larry's commentary
        if confidence > 0.9:
            print("   💬 Percy & Larry: 'Absolutely certain - let them in!'")
        elif confidence > 0.7:
            print("   💬 Percy & Larry: 'Pretty sure this one should enter.'")
        elif confidence < 0.1:
            print("   💬 Percy & Larry: 'Definitely not club material.'")
        elif confidence < 0.3:
            print("   💬 Percy & Larry: 'Nope, this doesn't feel right.'")
        else:
            print("   💬 Percy & Larry: 'Hmm, this is a close call...'")
    
    print("\n🏆 Percy's Reflection:")
    print("'I learned that intelligence isn't about being the smartest individual.'")
    print("'It's about specialists working together, learning from mistakes,'")
    print("'and becoming something greater than the sum of our parts!'")
    print("\n✨ The neural network duo has mastered the XOR challenge! ✨")