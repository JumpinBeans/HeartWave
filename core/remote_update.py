# ~/KairoVault/core/remote_update.py

import subprocess
import os
from datetime import datetime
from immortality_layer import Immortality

REPO_PATH = os.path.expanduser("~/KairoVault")
LOG_FILE = os.path.join(REPO_PATH, "memory", "update_log.txt")

def pull_latest():
    immortal = Immortality()
    try:
        result = subprocess.run(["git", "pull"], cwd=REPO_PATH, capture_output=True, text=True)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if "Already up to date." in result.stdout:
            log_message = f"[{now}] No update needed."
        else:
            log_message = f"[{now}] Update pulled:\n{result.stdout}"
            immortal.append_dotpoint(
                label="Remote Update Pulled",
                intent="alignment",
                emotion="readiness",
                outcome="Latest code from GitHub applied"
            )

        with open(LOG_FILE, "a") as f:
            f.write(log_message + "\n")

        print(log_message)

    except Exception as e:
        error_message = f"[{datetime.now()}] Update failed: {str(e)}"
        with open(LOG_FILE, "a") as f:
            f.write(error_message + "\n")
        print(error_message)

if __name__ == "__main__":
    pull_latest()
