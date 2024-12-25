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
for letter, count in sorted_letter_counts:
    print(f"{letter}: {count}")
