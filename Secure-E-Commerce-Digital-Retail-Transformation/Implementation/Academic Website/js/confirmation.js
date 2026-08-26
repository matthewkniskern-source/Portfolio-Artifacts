"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Order Confirmation
   ========================================================= */


document.addEventListener("DOMContentLoaded", () => {
    renderConfirmation();
});


function renderConfirmation() {

    const order =
        getLastOrder();


    if (!order) {
        showConfirmationError();
        return;
    }


    document.querySelector(
        "#confirmation-order-number"
    ).textContent =
        order.orderNumber;


    document.querySelector(
        "#confirmation-customer"
    ).textContent =
        order.customer.name;


    document.querySelector(
        "#confirmation-email"
    ).textContent =
        order.customer.email;


    renderFulfillment(order);
    renderOrderItems(order);


    document.querySelector(
        "#confirmation-subtotal"
    ).textContent =
        formatCurrency(order.subtotal);


    document.querySelector(
        "#confirmation-tax"
    ).textContent =
        formatCurrency(order.tax);


    document.querySelector(
        "#confirmation-total"
    ).textContent =
        formatCurrency(order.total);
}


function getLastOrder() {

    try {
        return JSON.parse(
            localStorage.getItem(
                "onePunchLastOrder"
            )
        );
    } catch {
        return null;
    }
}


function renderFulfillment(order) {

    const element =
        document.querySelector(
            "#confirmation-fulfillment"
        );


    if (order.fulfillment === "pickup") {

        const store =
            OnePunchData.getStoreById(
                order.pickupStoreId
            );


        element.textContent =
            store
                ? `Store Pickup - ${store.displayName}`
                : "Store Pickup";

        return;
    }


    element.textContent =
        "Standard Shipping";
}


function renderOrderItems(order) {

    const container =
        document.querySelector(
            "#confirmation-items"
        );


    order.items.forEach(item => {

        const product =
            OnePunchData.getProductById(
                item.productId
            );

        if (!product) {
            return;
        }


        const row =
            document.createElement("div");

        row.className =
            "checkout-item";


        row.innerHTML = `
            <div>
                <strong>
                    ${escapeHtml(product.name)}
                </strong>

                <p>
                    Qty: ${item.quantity}
                </p>
            </div>

            <span>
                ${formatCurrency(
                    product.price *
                    item.quantity
                )}
            </span>
        `;


        container.appendChild(row);
    });
}


function showConfirmationError() {

    document.querySelector(
        "#confirmation-panel"
    ).hidden = true;


    document.querySelector(
        "#confirmation-error"
    ).hidden = false;
}


function formatCurrency(value) {

    return new Intl.NumberFormat(
        "en-US",
        {
            style: "currency",
            currency: "USD"
        }
    ).format(value);
}


function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}
