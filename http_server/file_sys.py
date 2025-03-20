import os
import ujson  # JSON parsing and encoding module

# Define data to store as JSON
 
# Step 1: Write JSON data to a file
def save_data_to_file(data,filename="/data.json"):
    try:
        # Open the file in write mode ('w')
        with open(filename, "w") as file:
            # Write the JSON data to the file
            ujson.dump(data, file)
        print("Data saved to file.")
    except Exception as e:
        print(f"Error saving data to file: {e}")

# Step 2: Read JSON data from the file
def load_data_from_file(filename="/data.json"):
    try:
        # Open the file in read mode ('r')
        with open(filename, "r") as file:
            # Load the JSON data from the file
            loaded_data = ujson.load(file)
            print("Data loaded from file:", loaded_data)
            return loaded_data
    except OSError:
        print(f"Error reading file: {filename}")
        return None
    except Exception as e:
        print(f"Error loading data from file: {e}")
        return None