import sys
import json
import os

# Ensure a file path argument is provided
if len(sys.argv) < 2:
    print("Usage: python save_players.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]  # Get the file path from arguments

# Read JSON data from the file
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        players_data = json.load(file)  # Parse JSON
except json.JSONDecodeError as e:
    print(f"❌ Error decoding JSON: {e}")
    sys.exit(1)
except FileNotFoundError:
    print(f"❌ Error: File '{file_path}' not found.")
    sys.exit(1)

# Define the path where the updated player data will be stored
output_file = 'players.json'

# Check if the output file exists and read existing data
if os.path.exists(output_file):
    try:
        with open(output_file, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except json.JSONDecodeError:
        existing_data = {}  # If file is corrupted, start fresh
else:
    existing_data = {}

# Update the players list
existing_data['players'] = players_data

# Save the updated data back to the file
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(existing_data, file, indent=4, ensure_ascii=False)

print("✅ Players list updated successfully!")
