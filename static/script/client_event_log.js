let loggedNavigationInProgress = false;

// Scrit zum Loggen von Client-Events geschrieben von KI
function logClientEvent(event, extraInfo) {
    if (event !== 'add_to_favorites') {
        loggedNavigationInProgress = true;
    }
    fetch('/log_client_event', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            event: event,
            page: window.location.pathname,
            extra: extraInfo
        }),
        keepalive: true
    });
}

function logModalShown() {
    logClientEvent('modal_shown', null);
}
function logModalHomeButton() {
    logClientEvent('modal_home_button_pressed', null);
}

function logModalSearchButton() {
    logClientEvent('modal_search_button_pressed', null);
}

function logFavoriteNavButton() {
    logClientEvent('favorite_nav_button_pressed', null);
}

function logBasketNavButton() {
    logClientEvent('basket_nav_button_pressed', null);
}

function logHomeNavButton() {
    logClientEvent('home_nav_button_pressed', null);
}

function logAddFavorite(event_id) {
    logClientEvent('add_to_favorites', event_id);
}

function logBookButton(event_id) {
    logClientEvent('book_event_button_pressed', event_id);
}

function logBasketButton() {
    logClientEvent('basket_button_pressed', null);
}

function logHomeButton() {
    logClientEvent('home_button_pressed', null);
}

function logSearchButton() {
    const form = document.querySelector('.search_section');
    const formData = new FormData(form);
    const params = Object.fromEntries(formData.entries());
    logClientEvent('search_button_pressed', JSON.stringify(params));
}

function logOrderButton() {
    logClientEvent('order_button_pressed', null);
}

window.addEventListener('pagehide', () => {
    if (!loggedNavigationInProgress) {
        logClientEvent('browser_arrow_used');
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("flashOverlay");
    if (modal) {
        logModalShown();
    }
});