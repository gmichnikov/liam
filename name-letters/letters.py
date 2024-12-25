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
