"""
The Percy Chronicles: PyTorch Implementation
============================================

Percy's saga reimagined with PyTorch - the modern deep learning framework!

This is the same beloved story of Percy (hat specialist), Larry (glasses expert),
and Ada (decision maker) learning to solve the impossible XOR challenge, but now
powered by PyTorch's automatic differentiation magic.

For the full narrative, see the accompanying README.md file.
Young Padawan, witness how Percy's timeless wisdom translates to modern AI!
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Set random seeds for reproducible Percy adventures
torch.manual_seed(42)
np.random.seed(1)


# ==============================================================================
# Chapter 1: The Modern Magic - PyTorch Neural Network Architecture
# ==============================================================================


class XORClub(nn.Module):
    """
    The XOR Club itself - Percy, Larry, and Ada's establishment,
    now powered by PyTorch's modern neural architecture!

    This represents the complete club management system:
    - Percy and Larry as the specialist duo (hidden layer)
    - Ada as the final decision maker (output layer)
    - PyTorch handles the "whispers of wisdom" (backpropagation) automatically!
    """

    def __init__(self):
        super(XORClub, self).__init__()

        # Percy and Larry's specialist layer (2 inputs → 2 specialists)
        self.specialist_duo = nn.Linear(2, 2, bias=True)

        # Ada's decision layer (2 specialist opinions → 1 final decision)
        self.ada_decision = nn.Linear(2, 1, bias=True)

        # The excitement function (sigmoid activation)
        self.excitement = nn.Sigmoid()

        # Initialize weights like in our NumPy version for consistency
        with torch.no_grad():
            # Start with small random weights - like giving Percy and Larry
            # slightly different initial opinions
            self.specialist_duo.weight.normal_(0, 0.1)
            self.ada_decision.weight.normal_(0, 0.1)

            # Start biases at zero - no initial prejudices
            self.specialist_duo.bias.zero_()
            self.ada_decision.bias.zero_()

    def forward(self, guest_features):
        """
        Chapter 3: The Information Dance (PyTorch Style)

        Guest arrives → Percy & Larry analyze → Ada decides → Door opens/closes

        PyTorch makes this dance even more elegant with automatic computation graphs!
        """
        # Percy and Larry process the guest (hat and glasses status)
        specialist_opinions = self.excitement(self.specialist_duo(guest_features))

        # Ada makes the final decision based on her specialists' advice
        ada_raw_decision = self.ada_decision(specialist_opinions)
        final_confidence = self.excitement(ada_raw_decision)

        return final_confidence, specialist_opinions


# ==============================================================================
# Chapter 2: The Training Master - PyTorch's Automatic Learning
# ==============================================================================


def train_xor_club(model, X_train, y_train, epochs=2000, learning_rate=0.3):
    """
    Chapter 5: The Training Montage (PyTorch Edition)

    This is where Percy and Larry practice thousands of times with PyTorch's
    automatic differentiation handling the "whispers of wisdom" for us!

    No more manual backpropagation - PyTorch's autograd does the magic!
    """
    print("🤖 Percy and Larry begin their PyTorch training montage...")

    # Ada's mistake detector (loss function)
    grumpy_droid = nn.MSELoss()

    # The learning coordinator (optimizer) - manages how the team improves
    learning_coordinator = optim.SGD(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        total_error = 0

        # Practice with each training example
        for guest_features, correct_decision in zip(X_train, y_train):
            # Clear previous learning gradients
            learning_coordinator.zero_grad()

            # 1. PREDICT: What would we decide about this guest?
            ada_confidence, specialist_opinions = model(guest_features)

            # 2. MEASURE: How wrong were we? (The grumpy loss function)
            mistake_severity = grumpy_droid(ada_confidence, correct_decision)
            total_error += mistake_severity.item()

            # 3. LEARN: PyTorch automatically calculates the whispers of wisdom!
            mistake_severity.backward()  # Magic happens here!

            # 4. ADJUST: Apply the learning adjustments
            learning_coordinator.step()

        # Show the duo's progress every 100 rounds
        if (epoch + 1) % 100 == 0:
            avg_error = total_error / len(X_train)
            print(
                f"📊 Training Round {epoch + 1}/{epochs}, Team Error: {avg_error:.6f}"
            )


def examine_learned_wisdom(model):
    """
    Chapter 4: Examining the Learned Parameters (PyTorch Style)

    Let's peek at what Percy, Larry, and Ada learned through their PyTorch journey!
    """
    print("\n🎓 Training complete! Let's examine the learned wisdom...")
    print("\n🧠 Percy and Larry's Learned Parameters (PyTorch Edition):")
    print("=" * 60)

    # Extract Percy and Larry's learned expertise
    specialist_weights = model.specialist_duo.weight.data
    specialist_biases = model.specialist_duo.bias.data

    # Percy's learned preferences (first neuron)
    percy_hat_sensitivity = specialist_weights[0, 0].item()
    percy_glasses_opinion = specialist_weights[0, 1].item()
    percy_personal_bias = specialist_biases[0].item()

    # Larry's learned preferences (second neuron)
    larry_hat_opinion = specialist_weights[1, 0].item()
    larry_glasses_sensitivity = specialist_weights[1, 1].item()
    larry_personal_bias = specialist_biases[1].item()

    print("\n🎩 Percy (Hat Specialist) - PyTorch Learned Expertise:")
    print(f"   • Hat sensitivity: {percy_hat_sensitivity:.3f}")
    print(f"   • Glasses opinion: {percy_glasses_opinion:.3f}")
    print(f"   • Personal inclination: {percy_personal_bias:.3f}")

    print("\n👓 Larry (Glasses Expert) - PyTorch Learned Expertise:")
    print(f"   • Hat opinion: {larry_hat_opinion:.3f}")
    print(f"   • Glasses sensitivity: {larry_glasses_sensitivity:.3f}")
    print(f"   • Personal inclination: {larry_personal_bias:.3f}")

    # Extract Ada's learned trust relationships
    ada_weights = model.ada_decision.weight.data
    ada_bias = model.ada_decision.bias.data

    ada_trust_in_percy = ada_weights[0, 0].item()
    ada_trust_in_larry = ada_weights[0, 1].item()
    ada_personal_bias = ada_bias[0].item()

    print("\n👩‍💼 Ada (Decision Maker) - PyTorch Trust Relationships:")
    print(f"   • Trust in Percy's advice: {ada_trust_in_percy:.3f}")
    print(f"   • Trust in Larry's advice: {ada_trust_in_larry:.3f}")
    print(f"   • Decision-making bias: {ada_personal_bias:.3f}")

    print("\n💡 PyTorch Magic:")
    print("   • Automatic differentiation handled the 'whispers of wisdom'")
    print("   • Built-in optimizers managed the learning coordination")
    print("   • Computation graphs tracked every calculation automatically")


def opening_night_pytorch(model, X_test, y_test):
    """
    Chapter 6: Opening Night at The XOR Club (PyTorch Edition)

    Let's see how Percy, Larry, and Ada perform after their PyTorch training!
    """
    print("\n🚪 Opening night at The XOR Club (PyTorch Edition):")
    print("=" * 50)

    guest_types = [
        "Guest with no hat, no glasses",
        "Guest with no hat, but glasses",
        "Guest with hat, but no glasses",
        "Guest with both hat AND glasses",
    ]

    # Set model to evaluation mode (important for PyTorch)
    model.eval()

    with torch.no_grad():  # No gradients needed for evaluation
        for i, (guest_features, correct_decision) in enumerate(zip(X_test, y_test)):
            # Get the team's analysis
            ada_confidence, specialist_opinions = model(guest_features)

            # Extract individual opinions
            percy_excitement = specialist_opinions[0].item()
            larry_excitement = specialist_opinions[1].item()
            ada_confidence_value = ada_confidence.item()

            print(f"\n👤 {guest_types[i]}:")
            print(f"   🎩 Percy (Hat Specialist): {percy_excitement:.3f} excitement")
            print(f"   👓 Larry (Glasses Expert): {larry_excitement:.3f} excitement")
            print(f"   👩‍💼 Ada's confidence: {ada_confidence_value:.3f}")

            # Determine Ada's decision and check if it's correct
            ada_decision = "ACCEPT" if ada_confidence_value > 0.5 else "REJECT"
            correct_answer = "ACCEPT" if correct_decision.item() == 1 else "REJECT"
            is_correct = ada_decision == correct_answer

            print(f"   👩‍💼 Ada: ", end="")
            if ada_confidence_value > 0.8:
                print("'PyTorch training gave us crystal clarity!'")
            elif ada_confidence_value > 0.6:
                print("'The automatic gradients worked perfectly!'")
            elif ada_confidence_value < 0.2:
                print("'PyTorch clearly shows this guest doesn't fit.'")
            elif ada_confidence_value < 0.4:
                print("'The optimization process says no.'")
            else:
                print("'Even with PyTorch, some decisions are close calls.'")

            print(f"   👩‍💼 Ada's decision: {ada_decision}")
            print(f"   ✅ Correct answer: {correct_answer}")

            # Show Ada's performance
            if is_correct:
                print("   🎯 Ada's verdict: ✅ CORRECT! PyTorch mastery achieved!")
                print("   💼 Ada: 'Automatic differentiation is pure magic!'")
            else:
                print(
                    "   🎯 Ada's verdict: ❌ WRONG! Even PyTorch needs more practice..."
                )
                print("   💼 Ada: 'Time to adjust those hyperparameters!'")


# ==============================================================================
# Chapter 6: The PyTorch XOR Challenge
# ==============================================================================

if __name__ == "__main__":
    print("🎭 Welcome to The XOR Club - PyTorch Edition!")
    print("📖 Percy's timeless saga, now powered by modern deep learning...")
    print()

    # The XOR Challenge - same impossible problem, PyTorch solution
    X_train = torch.tensor(
        [
            [0.0, 0.0],  # No hat, no glasses → REJECT
            [0.0, 1.0],  # No hat, glasses → ACCEPT
            [1.0, 0.0],  # Hat, no glasses → ACCEPT
            [1.0, 1.0],  # Hat AND glasses → REJECT
        ],
        dtype=torch.float32,
    )

    y_train = torch.tensor(
        [
            [0.0],  # REJECT
            [1.0],  # ACCEPT
            [1.0],  # ACCEPT
            [0.0],  # REJECT
        ],
        dtype=torch.float32,
    )

    print("🧠 Building Percy's PyTorch team...")
    print("   - 2 input sensors (hat detector, glasses detector)")
    print("   - 2 hidden neurons (Percy and Larry as specialists)")
    print("   - 1 decision maker (Ada)")
    print("   - PyTorch autograd for automatic 'whispers of wisdom'")

    # Create Percy's PyTorch neural network
    percys_pytorch_club = XORClub()

    # Training parameters
    training_rounds = 2000
    learning_speed = 0.3

    print(f"\n🏋️ Beginning {training_rounds} rounds of PyTorch training...")
    print("(Percy and Larry will show progress every 100 rounds)")
    print()

    # Chapter 5: The PyTorch Training Montage
    train_xor_club(
        percys_pytorch_club, X_train, y_train, training_rounds, learning_speed
    )

    # Examine what the team learned
    examine_learned_wisdom(percys_pytorch_club)

    # Chapter 6: Opening Night Performance
    opening_night_pytorch(percys_pytorch_club, X_train, y_train)

    print("\n🏆 Percy's PyTorch Reflection:")
    print("'PyTorch showed me that the principles remain the same -'")
    print("'specialists working together, learning from mistakes,'")
    print("'but now with automatic differentiation magic!'")
    print("'Whether NumPy or PyTorch, intelligence is about partnership!'")
    print("\n✨ The neural network duo has mastered PyTorch! ✨")
