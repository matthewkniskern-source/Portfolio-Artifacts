"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Special Order Demonstration
   ========================================================= */


document.addEventListener("DOMContentLoaded", () => {
    populateStoreOptions();
    prefillProductRequest();
    initializeSpecialOrderForm();
});


/* =========================================================
   Store Options
   ========================================================= */

function populateStoreOptions() {

    const select =
        document.querySelector("#preferred-store");

    if (!select) {
        return;
    }

    OnePunchData.stores.forEach(store => {

        const option =
            document.createElement("option");

        option.value = store.id;
        option.textContent = store.displayName;

        select.appendChild(option);
    });
}


/* =========================================================
   Product Prefill
   ========================================================= */

function prefillProductRequest() {

    const params =
        new URLSearchParams(window.location.search);

    const productId =
        Number(params.get("id"));

    const productName =
        params.get("product");

    const itemField =
        document.querySelector("#requested-item");

    const franchiseField =
        document.querySelector("#franchise");


    if (productId) {

        const product =
            OnePunchData.getProductById(productId);

        if (product) {

            itemField.value =
                product.name;

            franchiseField.value =
                product.franchise;

            return;
        }
    }


    if (productName) {

        itemField.value =
            productName;
    }
}


/* =========================================================
   Form
   ========================================================= */

function initializeSpecialOrderForm() {

    const form =
        document.querySelector("#special-order-form");

    const newRequestButton =
        document.querySelector("#new-request");


    form.addEventListener(
        "submit",
        event => {

            event.preventDefault();

            clearErrors();

            if (!validateForm()) {
                return;
            }

            completeRequest();
        }
    );


    newRequestButton.addEventListener(
        "click",
        resetForm
    );
}


/* =========================================================
   Validation
   ========================================================= */

function validateForm() {

    let valid = true;

    const name =
        document.querySelector("#customer-name");

    const email =
        document.querySelector("#customer-email");

    const item =
        document.querySelector("#requested-item");


    if (!name.value.trim()) {

        showError(
            "customer-name",
            "Enter your name."
        );

        valid = false;
    }


    if (!email.value.trim()) {

        showError(
            "customer-email",
            "Enter your email address."
        );

        valid = false;

    } else if (!isValidEmail(email.value)) {

        showError(
            "customer-email",
            "Enter a valid email address."
        );

        valid = false;
    }


    if (!item.value.trim()) {

        showError(
            "requested-item",
            "Enter the item you are requesting."
        );

        valid = false;
    }


    return valid;
}


function isValidEmail(value) {

    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        .test(value.trim());
}


function showError(fieldId, message) {

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


function clearErrors() {

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
   Completion
   ========================================================= */

function completeRequest() {

    const form =
        document.querySelector("#special-order-form");

    const confirmation =
        document.querySelector(
            "#special-order-confirmation"
        );

    const requestNumber =
        document.querySelector("#request-number");


    requestNumber.textContent =
        generateRequestNumber();


    form.hidden = true;
    confirmation.hidden = false;


    confirmation.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}


function generateRequestNumber() {

    const randomPart =
        Math.floor(
            1000 +
            Math.random() * 9000
        );

    return `SO-${new Date().getFullYear()}-${randomPart}`;
}


/* =========================================================
   Reset
   ========================================================= */

function resetForm() {

    const form =
        document.querySelector("#special-order-form");

    const confirmation =
        document.querySelector(
            "#special-order-confirmation"
        );


    form.reset();

    clearErrors();

    confirmation.hidden = true;
    form.hidden = false;


    const cleanUrl =
        window.location.pathname;

    window.history.replaceState(
        {},
        "",
        cleanUrl
    );


    form.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}
