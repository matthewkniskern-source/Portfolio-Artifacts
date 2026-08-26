"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Contact Form
   ========================================================= */


document.addEventListener("DOMContentLoaded", () => {
    populateContactStores();
    initializeContactForm();
});


function populateContactStores() {

    const select =
        document.querySelector("#contact-store");


    OnePunchData.stores.forEach(store => {

        const option =
            document.createElement("option");

        option.value =
            store.id;

        option.textContent =
            store.displayName;

        select.appendChild(option);
    });
}


function initializeContactForm() {

    const form =
        document.querySelector("#contact-form");

    const newMessage =
        document.querySelector("#contact-new-message");


    form.addEventListener(
        "submit",
        event => {

            event.preventDefault();

            clearContactErrors();

            if (!validateContactForm()) {
                return;
            }

            completeContactRequest();
        }
    );


    newMessage.addEventListener(
        "click",
        resetContactForm
    );
}


function validateContactForm() {

    let valid = true;


    const name =
        document.querySelector("#contact-name");

    const email =
        document.querySelector("#contact-email");

    const message =
        document.querySelector("#contact-message");


    if (!name.value.trim()) {

        showContactError(
            "contact-name",
            "Enter your name."
        );

        valid = false;
    }


    if (!email.value.trim()) {

        showContactError(
            "contact-email",
            "Enter your email address."
        );

        valid = false;

    } else if (
        !/^[^\s@]+@[^\s@]+\.[^\s@]+$/
            .test(email.value.trim())
    ) {

        showContactError(
            "contact-email",
            "Enter a valid email address."
        );

        valid = false;
    }


    if (!message.value.trim()) {

        showContactError(
            "contact-message",
            "Enter a message."
        );

        valid = false;
    }


    return valid;
}


function showContactError(
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


function clearContactErrors() {

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


function completeContactRequest() {

    const form =
        document.querySelector("#contact-form");

    const confirmation =
        document.querySelector(
            "#contact-confirmation"
        );

    const reference =
        document.querySelector(
            "#contact-reference"
        );


    reference.textContent =
        generateContactReference();


    form.hidden = true;
    confirmation.hidden = false;


    confirmation.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}


function generateContactReference() {

    const random =
        Math.floor(
            1000 +
            Math.random() * 9000
        );


    return `CS-${new Date().getFullYear()}-${random}`;
}


function resetContactForm() {

    const form =
        document.querySelector("#contact-form");

    const confirmation =
        document.querySelector(
            "#contact-confirmation"
        );


    form.reset();

    clearContactErrors();

    confirmation.hidden = true;
    form.hidden = false;


    form.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}
