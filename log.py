import csv
from datetime import datetime

EVENT_LOG_FILE = "data/log.csv"

# Funktion öffnet und schreibt in die angegebene Datei für das Logging der Nutzerinteraktionen
# Die Datei darf während dem Programmablauf nicht geöffnet sein
def log_event(participant_id, condition, client, event, page="", extra=""):

    with open(EVENT_LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            participant_id,
            condition,
            datetime.now().isoformat(),
            client,
            event,
            page,
            extra
        ])