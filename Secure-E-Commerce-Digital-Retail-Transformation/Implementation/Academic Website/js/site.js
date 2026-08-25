"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Shared Site Behavior
   ========================================================= */


document.addEventListener("DOMContentLoaded", () => {
    initializeNavigation();
    updateCurrentYear();
    updateCartCount();
});


/* ---------- Mobile Navigation ---------- */

function initializeNavigation() {
    const toggle = document.querySelector(".nav-toggle");
    const navigation = document.querySelector(".primary-nav");

    if (!toggle || !navigation) {
        return;
    }

    toggle.addEventListener("click", () => {
        const isOpen = navigation.classList.toggle("is-open");

        toggle.setAttribute("aria-expanded", String(isOpen));
        toggle.textContent = isOpen ? "Close" : "Menu";
    });

    navigation.addEventListener("click", (event) => {
        if (!event.target.matches("a")) {
            return;
        }

        navigation.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "Menu";
    });
}


/* ---------- Footer Year ---------- */

function updateCurrentYear() {
    const yearElement = document.querySelector("#current-year");

    if (!yearElement) {
        return;
    }

    yearElement.textContent = new Date().getFullYear();
}


/* ---------- Cart Count ---------- */

function updateCartCount() {
    const cartCountElement = document.querySelector("#cart-count");

    if (!cartCountElement) {
        return;
    }

    let cart = [];

    try {
        cart = JSON.parse(localStorage.getItem("onePunchCart")) || [];
    } catch {
        cart = [];
    }

    const itemCount = cart.reduce((total, item) => {
        return total + Number(item.quantity || 0);
    }, 0);

    cartCountElement.textContent = itemCount;
    cartCountElement.setAttribute(
        "aria-label",
        `${itemCount} item${itemCount === 1 ? "" : "s"} in cart`
    );
}
