import random

# Create a list containing 10 numbers and 5 letters
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 elements from the list
winning_elements = random.sample(elements, 4)

# Print the message
print(f"Congratulations! Any ticket matching these 4 elements: {winning_elements} wins a prize!")