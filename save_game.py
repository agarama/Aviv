import sys
import json

file_path = "games.json"

def save_game(game_json):
    try:
        game_data = json.loads(game_json)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(game_data, f, indent=2, ensure_ascii=False)
        print("✅ המשחק נשמר בהצלחה!")
    except Exception as e:
        print(f"❌ שגיאה: {e}")

if __name__ == "__main__":
    save_game(sys.argv[1])
