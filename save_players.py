import sys
import json
import os

# Ensure a valid argument is provided
if len(sys.argv) < 2:
    print("Usage: python save_players.py <json_string>")
    sys.exit(1)

# Read JSON data from argument
try:
    players_data = json.loads(sys.argv[1])  # Parse JSON string
except json.JSONDecodeError as e:
    print(f"❌ Error decoding JSON: {e}")
    sys.exit(1)

# Define the path where the updated player data will be stored
output_file = 'players.json'

# Read existing data if available
if os.path.exists(output_file):
    try:
        with open(output_file, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except json.JSONDecodeError:
        existing_data = {}
else:
    existing_data = {}

# Update the players list
existing_data['players'] = players_data

# Save the updated data back to the file
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(existing_data, file, indent=4, ensure_ascii=False)

print("✅ Players list updated successfully!")
