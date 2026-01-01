import random

# Define a function to calculate love percentage
def love_percentage(name1, name2):
    # Calculate the sum of ASCII values of characters in names
    name1_sum = sum([ord(char) for char in name1.lower()])
    name2_sum = sum([ord(char) for char in name2.lower()])

    # Calculate love percentage
    love_percentage = (name1_sum + name2_sum) % 100

    print(f"{name1_sum} and {name2_sum}")
    # Return the love percentage
    return love_percentage

# Get names from the user
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

# Calculate the love percentage
love_percentage = love_percentage(name1, name2)

# Print the result
print(f"Your love percentage with {name2} is {love_percentage}%")

