import csv
from collections import defaultdict

# Dictionary to store number counts
number_counts = defaultdict(int)

# Read the CSV file
with open('numbers.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    
    # Count occurrences of each number
    for row in csv_reader:
        number = row['Number']
        number_counts[number] += 1

# Convert to sorted list of tuples (number, count) by count in descending order
retired_numbers_list = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)

# Print results
print("Number of times each number was retired:")
for number, count in retired_numbers_list:
    print(f"Number {number}: {count} time(s)")