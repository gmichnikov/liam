# Goal: Figure out the common letters in names (contain a letter)

# Step 1: Get a list of names

# Step 2: Count up how times each letter from a to z appears across all the names

import csv

# Filepath to your CSV file
csv_file = "name-counts.csv"

# Initialize an empty list to store the names
names = []

# Open and read the CSV file
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        names.append(row[0])  # Append the name (first column) to the list

# print(names)

# Create an empty dictionary to store letter counts
letter_counts = {}

# Loop through each name in the list
for name in names:
    # Loop through each character in the name
    for char in name.lower():  # Convert to lowercase for consistency
        # Check if the character is a letter
        if "a" <= char <= "z":
            # If the letter is already in the dictionary, increase its count
            if char in letter_counts:
                letter_counts[char] += 1
            # If the letter is not in the dictionary, add it with a count of 1
            else:
                letter_counts[char] = 1

# Sort the dictionary by values (counts) in descending order
sorted_letter_counts = sorted(
    letter_counts.items(), key=lambda item: item[1], reverse=True
)

# Print the sorted counts for each letter
print("Overall letter counts:")
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")

# Create an empty dictionary to store first-letter counts
first_letter_counts = {}

# Loop through each name in the list
for name in names:
    # Get the first letter of the name, converted to lowercase
    first_letter = name[0].lower()

    # Update the count for the first letter
    if first_letter in first_letter_counts:
        first_letter_counts[first_letter] += 1
    else:
        first_letter_counts[first_letter] = 1

# Print the counts for each first letter in descending order
print("\nFirst letter counts:")
for letter, count in sorted(
    first_letter_counts.items(), key=lambda item: item[1], reverse=True
):
    print(f"{letter}: {count}")

# Lists to store results
names_starting_with_y_or_u = []
names_with_j_not_first = []

# Loop through each name in the list
for name in names:
    # Check if the name starts with 'Y' or 'U'
    if name[0].lower() in ["y", "u"]:
        names_starting_with_y_or_u.append(name)

    # Check if the name has 'J' that is not the first character
    if "j" in name[1:].lower():  # Skip the first character when checking
        names_with_j_not_first.append(name)

# Print the results
print()
print("Names starting with Y or U:", names_starting_with_y_or_u)
print("Names with J not first:", names_with_j_not_first)
