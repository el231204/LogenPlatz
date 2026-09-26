# Sammlung aller Fehlermeldungen, um einheitliche Formulierungen zu gewährleisten

MESSAGES = {
    "few_remaining_sold_out": {
        "error_design_1": {
            "title": "Fehler",
            "paragraphs": [
                "Ticket nicht buchbar.",
            ],
        },
        "error_design_2": {
            "title": "Knapp verpasst!",
            "paragraphs": [
                "Dieses Event ist inzwischen komplett ausgebucht und kann daher nicht mehr dem Warenkorb hinzugefügt werden.",
                "Vielleicht findest du eine ähnliche Veranstaltung, die dir genauso gut gefällt?",
            ],
        },
    },
    "sold_out": {
        "error_design_1": {
            "title": "Fehler",
            "paragraphs": [
                "Ticket nicht buchbar.",
            ],
        },
        "error_design_2": {
            "title": "Ausverkauft!",
            "paragraphs": [
                "Da dieses Event bereits komplett ausgebucht ist, kann es leider nicht mehr dem Warenkorb hinzugefügt werden.",
                "Vielleicht findest du eine ähnliche Veranstaltung, die dir genauso gut gefällt?",
            ],
        },
    },
    "basket_timeout": {
        "error_design_1": {
            "title": "Fehler",
            "paragraphs": [
                "Zeitlimit abgelaufen."
            ],
        },
        "error_design_2": {
            "title": "Warenkorb zurückgesetzt",
            "paragraphs": [
                "Kein Problem. Die Zeit für die Reservierung deines Warenkorbs ist abgelaufen.",
                "Leg die gewünschten Events gerne erneut in den Warenkorb.",
            ],
        },
    },
}


def get_message(key, condition):
    return MESSAGES[key][condition]
