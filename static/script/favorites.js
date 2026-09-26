// Skript um den Favoriten-Button nach dem Klick zu markieren und die Favoriten in sessionStorage zu speichern, geschrieben von KI

document.addEventListener("DOMContentLoaded", () => {
    const favorites = JSON.parse(sessionStorage.getItem("favorites") || "[]");

    document.querySelectorAll(".favorite[data-event-id]").forEach((btn) => {
        const id = btn.dataset.eventId;

        // Beim Laden: bereits favorisierte Events markieren
        if (favorites.includes(id)) {
            btn.classList.add("active");
        }

        btn.addEventListener("click", () => toggleFavorite(btn, id));
    });
});

function toggleFavorite(btn, id) {
    let favorites = JSON.parse(sessionStorage.getItem("favorites") || "[]");

    if (favorites.includes(id)) {
        favorites = favorites.filter((f) => f !== id);
        btn.classList.remove("active");
    } else {
        favorites.push(id);
        btn.classList.add("active");
    }

    sessionStorage.setItem("favorites", JSON.stringify(favorites));

    // Bestehendes Logging weiterhin auslösen, falls vorhanden
    if (typeof logAddFavorite === "function") {
        logAddFavorite(id);
    }
}