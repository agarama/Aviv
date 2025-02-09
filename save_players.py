import sys
import json
import os

# Load player data from the arguments
players_json = sys.argv[1]  # This will get the playersJson passed from GitHub Actions

# Convert the JSON string to a Python object
players_data = json.loads(players_json)

# Define the path where you want to store the player data
file_path = 'players.json'  # You can change this to any file in your repo

# Check if the file exists
if os.path.exists(file_path):
    # If it exists, read its contents first (optional, for additional processing)
    with open(file_path, 'r') as file:
        existing_data = json.load(file)
else:
    existing_data = {}

# Update the file with the new player list
existing_data['players'] = players_data

# Save the updated data back to the file
with open(file_path, 'w') as file:
    json.dump(existing_data, file, indent=4)
