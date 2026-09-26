import json
import random

EVENTS_FILE = "data/events.json"
# Funktion zum Laden der Events aus der JSON-Datei
def load_events():
    try:
        with open(EVENTS_FILE, "r", encoding="utf-8") as file:
            events = json.load(file)
    except FileNotFoundError:
        events = []
    return events
ALL_EVENTS = load_events()

# Funktion zum Erstellen der gefilteren Eventliste basierend auf den Suchkriterien
def filter_events(search_bar, genre, location, date, dress_code, category):

    filtered_events = []
    
    for event in ALL_EVENTS:

        event_title = event["title"]
        event_description = event["description"]
        event_location = event["location"] 
        event_genre = event["genre"]
        event_date = event["date"]
        event_dress_code = event["dress_code"]
        event_category = event["type"]

        if search_bar:
            query = search_bar.lower()
            if (query not in event_title.lower() and query not in event_description.lower()):
                continue 
        if location:
            if location.lower() != event_location.lower():
                continue
        if genre:
            if genre.lower() != event_genre.lower():
                continue
        if date:
            if date != event_date:
                continue
        if dress_code:
            if dress_code.lower() != event_dress_code.lower():
                continue
        if category:
            if category.lower() != event_category.lower():
                continue
        filtered_events.append(event)

    return filtered_events

# Funktion zum Abrufen einer zufälligen Auswahl von Events für die Startseite
def get_random_events(num_events=4):
    if num_events > len(ALL_EVENTS):
        num_events = len(ALL_EVENTS)
    return random.sample(ALL_EVENTS, num_events)

# Funktion zum Abrufen eines bestimmten Events basierend auf der Event-ID
def get_event_by_id(event_id):
    for event in ALL_EVENTS:
        if event["id"] == event_id:
            return event
    return None
