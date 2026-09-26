from decimal import Decimal
from functools import partial
import os

from flask import Flask, flash, redirect, render_template, request, url_for
from error_messages import get_message
from event_data_handler import filter_events, get_event_by_id, get_random_events
from log import log_event

app = Flask(__name__)
app.secret_key = "secret_key"  # Session-Key für Flash-Meldungen

PARTICIPANT_ID = os.environ.get("PARTICIPANT_ID", "1_test")
CONDITION = os.environ.get("CONDITION", "error_design_1")

basket = []
order_counter = 0 

# Partial-Funktion um participant_id und condition in allen Aufrufen von log_event automatisch zu übergeben, geschrieben von KI
log_event = partial(log_event, participant_id=PARTICIPANT_ID, condition=CONDITION, client="server")

# Übergabe der Variable an die Templates für die Anzeige des entsprechenden Designs, geschrieben von KI
@app.context_processor
def inject_condition():
    return dict(condition=CONDITION)


# Routen für die Seiten und Logik
@app.route("/")
@app.route("/home", methods=["GET"])
def home():
    events = get_random_events(num_events=4)
    log_event(event="page_visit",page="home_page",
        extra="Events displayed: {}".format([event["title"] for event in events]),)
    return render_template("home.html", events=events)


@app.route("/search_results", methods=["GET"])
def search_results():
    search_bar = request.args.get("search_bar", default="")
    genre = request.args.get("genre", default="")
    location = request.args.get("location", default="")
    date = request.args.get("date", default="")
    dress_code = request.args.get("dress_code", default="")
    category = request.args.get("category", default="")

    filtered_events = filter_events(
        search_bar, genre, location, date, dress_code, category
    )
    event_count = len(filtered_events)

    log_event(event="page_visit", page="search_results",
        extra="Search parameters: search_bar={} genre={} location={} date={} dress_code={} category={} Event count: {}".format(
            search_bar, genre, location, date, dress_code, category, event_count),)
    return render_template("search_results.html", events=filtered_events)


@app.route("/details/<int:event_id>", methods=["GET"])
def details(event_id):
    event = get_event_by_id(event_id)
    log_event(event="page_visit", page="details_page",
        extra="Event: id{}, {}, {}, {}, {}, {}".format(
            event["id"],
            event["title"],
            event["location"],
            event["genre"],
            event["date"],
            event["dress_code"],),)
    return render_template("details.html", event=event)


@app.route("/success/<info>", methods=["GET"])
def success(info):
    global basket
    if info == "added_to_basket":
        item = basket[-1]["title"] 
        log_event(event="page_visit", page="success",
            extra="Event {} wurde zum Warenkorb hinzugefügt.".format(item),)
        message = f"Das Event<br>{item}<br>wurde erfolgreich zum Warenkorb hinzugefügt."
        show_basket=True
    elif info == "order_completed":
        log_event(event="page_visit", page="success",
            extra="basket contents: {}".format([event["title"] for event in basket]),)
        basket.clear()
        message = "Vielen Dank für Ihre Bestellung!<br>Ihr Einkauf war erfolgreich."
        show_basket=False
    return render_template("success.html", message=message, basket=show_basket)


@app.route("/add_to_basket", methods=["POST"])
def add_to_basket():
    global basket
    event_id = int(request.form.get("event_id"))
    event = get_event_by_id(event_id)
    event_state = event.get("state")
    luck = None

    if event_state == "few_remaining":
        luck = event.get("outcome")

    if event_state == "sold_out" or luck == "sold_out":
        if luck:
            log_event(event="add_to_basket_failed", page="",
                extra="Event ID: {} is sold out from few remaining".format(event_id))
            flash(get_message("few_remaining_sold_out", CONDITION))
        else:
            log_event(event="add_to_basket_failed", page="",
                extra="Event ID: {} is sold out".format(event_id))
            flash(get_message("sold_out", CONDITION))
        return redirect(url_for("details", event_id=event_id, **request.args.to_dict()))
    
    basket.append(event)
    log_event(event="add_to_basket", page="",
        extra="Event ID: {}".format(event_id),)
    return redirect(url_for("success", info="added_to_basket"))


@app.route("/basket", methods=["GET"])
def basket_page():
    global basket
    total_price = sum(
        Decimal(event["price"].replace(",", "."))
        for event in basket
    )
    total_price_str = str(total_price).replace(".", ",")
    log_event(event="page_visit", page="basket_page",
        extra="basket contents: {}, Preis: {}".format([event["title"] for event in basket], total_price),)
    return render_template("basket.html", basket=basket, total_price=total_price_str)


@app.route("/complete_order", methods=["GET"])
def complete_order():
    global basket
    global order_counter
    order_counter += 1
    if order_counter % 2 == 0:
        basket.clear()
        log_event(event="basket_emptied", page="basket",
            extra="Order {}".format(order_counter),)

    if len(basket) == 0:
        log_event(event="order_failed", page="basket",
            extra="Empty basket after timeout",)
        flash(get_message("basket_timeout", CONDITION))
        return redirect(url_for("basket_page"))

    log_event(event="order_successful", page="basket",
        extra="",)
    return redirect(url_for('success', info='order_completed'))


# Route um clientseitige Events zu loggen, geschrieben von KI
@app.route('/log_client_event', methods=['POST'])
def log_client_event():
    data = request.get_json() or {}
    log_event(client="client", event=data.get('event'), page=data.get('page'), 
        extra=data.get('extra'),)
    return "", 204


# Error Handling - 404 Seite unterschiedliche je nach Design 1 oder 2
@app.errorhandler(404)
def page_not_found(e):
    log_event(event="page_visit", page="404_error",
        extra=e,)
    if CONDITION == "error_design_1":
        return render_template("404_1.html"), 404
    elif CONDITION == "error_design_2":
        return render_template("404_2.html"), 404