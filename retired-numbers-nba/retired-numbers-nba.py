import csv
from collections import defaultdict
import matplotlib.pyplot as plt

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

# Visualization
numbers = [int(num) for num, count in retired_numbers_list]
counts = [count for num, count in retired_numbers_list]

plt.figure(figsize=(10, 6))
plt.bar(numbers, counts, color='skyblue')
plt.xlabel('Number')
plt.ylabel('Count')
plt.title('Number of Times Each Number Was Retired')
plt.xticks(numbers)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Increase the number of tick marks on the y-axis
max_count = max(counts)
plt.yticks(range(0, max_count + 1, 1))

plt.show()