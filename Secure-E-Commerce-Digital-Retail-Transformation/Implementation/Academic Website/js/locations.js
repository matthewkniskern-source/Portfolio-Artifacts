"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Store Locations
   ========================================================= */


document.addEventListener("DOMContentLoaded", () => {
    renderLocations();
});


function renderLocations() {

    const container =
        document.querySelector("#locations-grid");


    if (!container) {
        return;
    }


    OnePunchData.stores.forEach(store => {

        const card =
            document.createElement("article");

        card.className =
            "location-card";


        card.innerHTML = `
            <div class="location-card-header">

                <p class="eyebrow">
                    Chico, California
                </p>

                <h2>
                    ${escapeHtml(store.name)}
                </h2>

            </div>


            <div class="location-details">

                <div>
                    <h3>Address</h3>

                    <p>
                        ${escapeHtml(store.addressLine1)}<br>
                        ${escapeHtml(store.city)},
                        ${escapeHtml(store.state)}
                        ${escapeHtml(store.postalCode)}
                    </p>
                </div>


                <div>
                    <h3>Phone</h3>

                    <p>
                        ${escapeHtml(store.phone)}
                    </p>
                </div>


                <div>
                    <h3>Store Hours</h3>

                    <dl class="store-hours">

                        <div>
                            <dt>Mon - Thu</dt>
                            <dd>
                                ${escapeHtml(
                                    store.hours.mondayThursday
                                )}
                            </dd>
                        </div>

                        <div>
                            <dt>Fri - Sat</dt>
                            <dd>
                                ${escapeHtml(
                                    store.hours.fridaySaturday
                                )}
                            </dd>
                        </div>

                        <div>
                            <dt>Sunday</dt>
                            <dd>
                                ${escapeHtml(
                                    store.hours.sunday
                                )}
                            </dd>
                        </div>

                    </dl>
                </div>

            </div>


            <div class="location-card-actions">

                <a
                    class="button button-primary"
                    href="products.html"
                >
                    Check Inventory
                </a>

            </div>
        `;


        container.appendChild(card);
    });
}


function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}
