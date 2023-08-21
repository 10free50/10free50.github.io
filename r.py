import random
import string

# Function to generate a random string
def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits + string.ascii_lowercase
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Number of lines in each text file
num_lines = 50000

# Number of text files
num_files = 5

# Base URL
base_url = "https://10free50.github.io/?keyword="

# Generate and write URLs to text files
for file_num in range(num_files):
    file_name = f"url_file_{file_num + 1}.txt"
    with open(file_name, 'w') as file:
        for _ in range(num_lines):
            random_code = generate_random_string(10)  # Adjust the length as needed
            url = base_url + random_code + "\n"
            file.write(url)

print("URLs generated and written to text files.")
