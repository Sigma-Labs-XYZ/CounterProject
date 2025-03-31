# Import necessary libraries
import random
import string
import json

# Generate a random string
def generate_random_string(length=10):
    'Generates A random string of specified length or length 10 by default.'
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Function to create a list of random numbers
def generate_random_numbers(count=10):
    'generates a random number from  0 t o 100'
    return [random.randint(0, 100) for _ in range(count)]

# Calculate the average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Find the maximum number in a list
def find_maximum(numbers):
    return max(numbers) if numbers else None

# Write data to a file
def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)

# Read data from a file
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

# Create a dictionary of random data
def create_random_data_dict():
    return {
        "random_string": generate_random_string(),
        "random_numbers": generate_random_numbers(),
        "average": None,
        "maximum": None
    }

def does_nothing():
    'function does nothing'
    for i in range(100):
        pass

# Update the dictionary with average and maximum
def update_data_dict(data):
    'updates data in the dictionary to include average and maximum out of the data'
    numbers = data.get("random_numbers", [])
    data["average"] = calculate_average(numbers)
    data["maximum"] = find_maximum(numbers)

# Main function to demonstrate functionality
def main():
    # Create a dictionary with random data
    data_dict = create_random_data_dict()

    # Update the dictionary with calculated values
    update_data_dict(data_dict)

    # Write the dictionary to a file
    write_to_file('data.json', json.dumps(data_dict))

    # Read the data back from the file
    retrieved_data = read_from_file('data.json')

    # Display the retrieved data
    if retrieved_data:
        print("Retrieved Data:")
        print(json.loads(retrieved_data))
    else:
        print("No data found.")

# Run the main function
if __name__ == "__main__":
    main()