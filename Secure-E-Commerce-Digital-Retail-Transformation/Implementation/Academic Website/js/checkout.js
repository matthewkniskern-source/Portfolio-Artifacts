
"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Checkout Demonstration
   ========================================================= */


const CHECKOUT_TAX_RATE = 0.065;


document.addEventListener("DOMContentLoaded", () => {
    initializeCheckout();
});


function initializeCheckout() {

    const cart = getCheckoutCart();

    if (cart.length === 0) {
        window.location.href = "cart.html";
        return;
    }

    populatePickupStores();
    renderCheckoutSummary(cart);
    initializeFulfillmentControls();
    initializeCheckoutForm(cart);
}


/* =========================================================
   Cart
   ========================================================= */

function getCheckoutCart() {

    try {
        return JSON.parse(
            localStorage.getItem("onePunchCart")
        ) || [];
    } catch {
        return [];
    }
}


/* =========================================================
   Pickup Stores
   ========================================================= */

function populatePickupStores() {

    const select =
        document.querySelector("#pickup-store");

    OnePunchData.stores.forEach(store => {

        const option =
            document.createElement("option");

        option.value = store.id;
        option.textContent = store.displayName;

        select.appendChild(option);
    });
}


/* =========================================================
   Fulfillment
   ========================================================= */

function initializeFulfillmentControls() {

    const fulfillment =
        document.querySelector("#fulfillment-method");

    const pickupField =
        document.querySelector("#pickup-store-field");


    fulfillment.addEventListener(
        "change",
        () => {

            pickupField.hidden =
                fulfillment.value !== "pickup";
        }
    );
}


/* =========================================================
   Summary
   ========================================================= */

function renderCheckoutSummary(cart) {

    const container =
        document.querySelector("#checkout-items");

    let subtotal = 0;


    cart.forEach(item => {

        const product =
            OnePunchData.getProductById(
                item.productId
            );

        if (!product) {
            return;
        }


        const lineTotal =
            product.price * item.quantity;

        subtotal += lineTotal;


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
                ${formatCurrency(lineTotal)}
            </span>
        `;


        container.appendChild(row);
    });


    const tax =
        subtotal * CHECKOUT_TAX_RATE;

    const total =
        subtotal + tax;


    document.querySelector(
        "#checkout-subtotal"
    ).textContent =
        formatCurrency(subtotal);


    document.querySelector(
        "#checkout-tax"
    ).textContent =
        formatCurrency(tax);


    document.querySelector(
        "#checkout-total"
    ).textContent =
        formatCurrency(total);
}


/* =========================================================
   Form
   ========================================================= */

function initializeCheckoutForm(cart) {

    const form =
        document.querySelector("#checkout-form");


    form.addEventListener(
        "submit",
        event => {

            event.preventDefault();

            clearCheckoutErrors();

            if (!validateCheckoutForm()) {
                return;
            }

            createOrder(cart);
        }
    );
}


/* =========================================================
   Validation
   ========================================================= */

function validateCheckoutForm() {

    let valid = true;


    const requiredFields = [
        ["checkout-name", "Enter your name."],
        ["checkout-email", "Enter your email address."],
        ["checkout-address", "Enter a street address."],
        ["checkout-city", "Enter a city."],
        ["checkout-state", "Enter a state abbreviation."],
        ["checkout-zip", "Enter a ZIP code."],
        ["card-number", "Enter a demonstration card number."],
        ["card-expiration", "Enter an expiration date."],
        ["card-cvv", "Enter a CVV."]
    ];


    requiredFields.forEach(
        ([fieldId, message]) => {

            const field =
                document.querySelector(
                    `#${fieldId}`
                );

            if (!field.value.trim()) {

                showCheckoutError(
                    fieldId,
                    message
                );

                valid = false;
            }
        }
    );


    const email =
        document.querySelector(
            "#checkout-email"
        ).value;


    if (
        email &&
        !/^[^\s@]+@[^\s@]+\.[^\s@]+$/
            .test(email.trim())
    ) {

        showCheckoutError(
            "checkout-email",
            "Enter a valid email address."
        );

        valid = false;
    }


    const state =
        document.querySelector(
            "#checkout-state"
        ).value.trim();


    if (
        state &&
        !/^[A-Za-z]{2}$/.test(state)
    ) {

        showCheckoutError(
            "checkout-state",
            "Use a two-letter state abbreviation."
        );

        valid = false;
    }


    const zip =
        document.querySelector(
            "#checkout-zip"
        ).value.trim();


    if (
        zip &&
        !/^\d{5}(-\d{4})?$/.test(zip)
    ) {

        showCheckoutError(
            "checkout-zip",
            "Enter a valid ZIP code."
        );

        valid = false;
    }


    const cardNumber =
        document.querySelector(
            "#card-number"
        ).value.replace(/\s/g, "");


    if (
        cardNumber &&
        !/^\d{16}$/.test(cardNumber)
    ) {

        showCheckoutError(
            "card-number",
            "Use a 16-digit fictional card number."
        );

        valid = false;
    }


    const expiration =
        document.querySelector(
            "#card-expiration"
        ).value.trim();


    if (
        expiration &&
        !/^(0[1-9]|1[0-2])\/\d{2}$/
            .test(expiration)
    ) {

        showCheckoutError(
            "card-expiration",
            "Use MM/YY format."
        );

        valid = false;
    }


    const cvv =
        document.querySelector(
            "#card-cvv"
        ).value.trim();


    if (
        cvv &&
        !/^\d{3,4}$/.test(cvv)
    ) {

        showCheckoutError(
            "card-cvv",
            "Use a 3 or 4 digit fictional CVV."
        );

        valid = false;
    }


    return valid;
}


function showCheckoutError(
    fieldId,
    message
) {

    const field =
        document.querySelector(
            `#${fieldId}`
        );

    const error =
        document.querySelector(
            `#${fieldId}-error`
        );


    field.setAttribute(
        "aria-invalid",
        "true"
    );

    error.textContent =
        message;
}


function clearCheckoutErrors() {

    document
        .querySelectorAll(".field-error")
        .forEach(error => {
            error.textContent = "";
        });


    document
        .querySelectorAll("[aria-invalid='true']")
        .forEach(field => {
            field.removeAttribute(
                "aria-invalid"
            );
        });
}


/* =========================================================
   Order Creation
   ========================================================= */

function createOrder(cart) {

    const totals =
        calculateOrderTotals(cart);


    const fulfillment =
        document.querySelector(
            "#fulfillment-method"
        ).value;


    const order = {

        orderNumber:
            generateOrderNumber(),

        createdAt:
            new Date().toISOString(),

        customer: {
            name:
                document.querySelector(
                    "#checkout-name"
                ).value.trim(),

            email:
                document.querySelector(
                    "#checkout-email"
                ).value.trim()
        },

        shippingAddress: {
            address:
                document.querySelector(
                    "#checkout-address"
                ).value.trim(),

            city:
                document.querySelector(
                    "#checkout-city"
                ).value.trim(),

            state:
                document.querySelector(
                    "#checkout-state"
                ).value.trim().toUpperCase(),

            zip:
                document.querySelector(
                    "#checkout-zip"
                ).value.trim()
        },

        fulfillment,

        pickupStoreId:
            fulfillment === "pickup"
                ? document.querySelector(
                    "#pickup-store"
                ).value
                : null,

        items: cart,

        subtotal:
            totals.subtotal,

        tax:
            totals.tax,

        total:
            totals.total
    };


    localStorage.setItem(
        "onePunchLastOrder",
        JSON.stringify(order)
    );


    localStorage.removeItem(
        "onePunchCart"
    );


    window.location.href =
        "confirmation.html";
}


/* =========================================================
   Totals
   ========================================================= */

function calculateOrderTotals(cart) {

    let subtotal = 0;


    cart.forEach(item => {

        const product =
            OnePunchData.getProductById(
                item.productId
            );

        if (!product) {
            return;
        }


        subtotal +=
            product.price *
            item.quantity;
    });


    const tax =
        subtotal * CHECKOUT_TAX_RATE;

    const total =
        subtotal + tax;


    return {
        subtotal,
        tax,
        total
    };
}


/* =========================================================
   Helpers
   ========================================================= */

function generateOrderNumber() {

    const random =
        Math.floor(
            10000 +
            Math.random() * 90000
        );

    return `OP-${new Date().getFullYear()}-${random}`;
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
