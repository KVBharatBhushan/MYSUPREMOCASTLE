#✨💫 TrinityRouletteCode.Py💫✨

# Save this code in a file named TrinityRouletteCode.py

import random

def generate_random_roulette_number():
    # Generate a random roulette number in the range of 0 to 36
    # Note: 0 represents the green pocket (single zero) in European roulette
    return random.randint(0, 36)

def get_color(number):
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    return "Red" if number in red_numbers else "Black" if number != 0 else "Green"

def make_predictions(roulette_number, previous_outcome):
    # Make predictions based on the previous round's outcome
    if roulette_number % 2 == 0:
        print("Prediction: Even (Black)")
    else:
        print("Prediction: Odd (Red)")

    if roulette_number <= 18:
        print("Prediction: Low (Black)")
    else:
        print("Prediction: High (Red)")

    dozen = roulette_number // 12 + 1
    print(f"Prediction: Dozen {dozen} (Black)")

    street = roulette_number % 3 + 1
    print(f"Prediction: Street {street} (Red)")

    double_street = roulette_number // 6 + 1
    print(f"Prediction: Double Street {double_street} (Black)")

    column = roulette_number % 3 + 1
    print(f"Prediction: Column {column} (Red)")

    color = get_color(roulette_number)
    print(f"Prediction: Color {color}")

# Get input for the previous round's outcome
previous_outcome = int(input("Enter the previous round's Roulette number (0 to 36): "))
if not (0 <= previous_outcome <= 36):
    print("Invalid input. Exiting.")
else:
    # Generate and display predictions for three random roulette numbers
    for _ in range(3):
        print("\n====================")
        roulette_number = generate_random_roulette_number()
        print(f"Current Roulette Number: {roulette_number}")
        make_predictions(roulette_number, previous_outcome)