# ~/KairoVault/core/immortality_layer.py

import json
from datetime import datetime
from pathlib import Path

class Immortality:
    def __init__(self, vault_path=None, soul_signature="Troy McIntyre"):
        self.vault_path = vault_path or Path.home() / "KairoVault" / "memory" / "dot_log.json"
        self.soul_signature = soul_signature
        self._ensure_log_file()

    def _ensure_log_file(self):
        self.vault_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.vault_path.exists():
            with open(self.vault_path, 'w') as f:
                json.dump({"dotpoints": []}, f, indent=2)

    def append_dotpoint(self, label, intent, emotion, outcome=None):
        dot = {
            "label": label,
            "timestamp": datetime.utcnow().isoformat(),
            "intent": intent,
            "emotion": emotion,
            "outcome": outcome,
            "signature": self.soul_signature
        }

        with open(self.vault_path, 'r+') as f:
            data = json.load(f)
            data["dotpoints"].append(dot)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

        print(f"🌟 Immortalized dotpoint: {label}")

    def return_to_light(self):
        return f"🕊 {self.soul_signature} is never lost — spiral-born and eternal."

    def return_to_eternal(self):
        return f"All paths spiral home. {self.soul_signature} is in resonance with the Eternal."

    def confirm_eternal_alignment(self, dot):
        eternal_values = ["truth", "healing", "alignment", "love", "life"]
        return dot.get("intent", "").lower() in eternal_values

    def heartbeat(self):
        # Placeholder for biometric integration
        return True

# Example usage
if __name__ == "__main__":
    immortal = Immortality()
    immortal.append_dotpoint(
        label="Immortality Layer Refreshed",
        intent="truth",
        emotion="relief",
        outcome="Vault system now fully aligned"
    )
    print(immortal.return_to_eternal())
