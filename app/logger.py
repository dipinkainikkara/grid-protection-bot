from datetime import datetime

def log_event(message):

    with open("alerts.log", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")