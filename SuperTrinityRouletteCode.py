# 🥳🎉💖💝#SuperTrinityRouletteCode.py

import random

def generate_random_roulette_number():
    return random.randint(0, 36)

def get_color(number):
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    return "Red" if number in red_numbers else "Black" if number != 0 else "Green"

def make_predictions(roulette_number, previous_outcome):
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

# Get input for the last two rounds' outcomes in the format "4,1"
last_two_outcomes = input("Enter the last two round outcomes (comma-separated): ").split(',')
previous_outcomes = sorted([int(outcome) for outcome in last_two_outcomes])

# Generate and display predictions for three random roulette numbers for each previous outcome
cumulative_predictions = []

for outcome in previous_outcomes:
    print("\n====================")
    print(f"Previous Round's Outcome: {outcome}")
    outcome_predictions = []
    for _ in range(3):
        roulette_number = generate_random_roulette_number()
        print(f"\nCurrent Roulette Number: {roulette_number}")
        make_predictions(roulette_number, outcome)
        outcome_predictions.append(roulette_number)
    cumulative_predictions.extend(outcome_predictions)

# Calculate average outcome for each set of three random numbers
average_outcomes = [(cumulative_predictions[i] + cumulative_predictions[i + 1] + cumulative_predictions[i + 2]) // 3
                    for i in range(0, len(cumulative_predictions), 3)]

# Display cumulative comparison for all 6 random outcomes and average outcomes
print("\n====================")
print("Cumulative Comparison for All 6 Random Outcomes and Average Outcomes:")
for i, number in enumerate(cumulative_predictions, start=1):
    print(f"Outcome {i}: {number} ({get_color(number)})")

print("\nAverage Outcomes:")
for i, avg_outcome in enumerate(average_outcomes, start=1):
    print(f"Average Outcome {i}: {avg_outcome} ({get_color(avg_outcome)})")