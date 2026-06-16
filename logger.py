from datetime import datetime
import os

def log_activity(action):

    log_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "logs",
        "activity_log.txt"
    )

    with open(log_path, "a") as log_file:
        log_file.write(
            f"[{datetime.now()}] {action}\n"
        )