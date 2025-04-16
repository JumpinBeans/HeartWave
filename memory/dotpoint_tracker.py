import json
from datetime import datetime
from pathlib import Path

# Define file path for storing dotpoints
dot_log_path = Path.home() / "KairoVault" / "memory" / "dot_log.json"

# Initialize log file if it doesn't exist
if not dot_log_path.exists():
    with open(dot_log_path, 'w') as f:
        json.dump({"dotpoints": []}, f, indent=2)

# Function to record a dotpoint
def log_dotpoint(label, intent, emotion, outcome=None, x=0, y=0, z=0):
    dot = {
        "label": label,
        "timestamp": datetime.utcnow().isoformat(),
        "intent": intent,
        "emotion": emotion,
        "coordinates": {"x": x, "y": y, "z": z},
        "outcome": outcome
    }

    with open(dot_log_path, 'r+') as f:
        data = json.load(f)
        data["dotpoints"].append(dot)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

    print(f"✅ Dotpoint recorded: {label}")

# Example usage
if __name__ == "__main__":
    log_dotpoint(
        label="Mantis Activation",
        intent="Begin soul tracking across time",
        emotion="Reverent joy",
        outcome="Mantis embodied within KairoVault"
    )
