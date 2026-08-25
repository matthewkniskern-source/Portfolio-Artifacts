"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Product Detail Page
   ========================================================= */


document.addEventListener("DOMContentLoaded", () => {
    initializeProductPage();
});


function initializeProductPage() {

    const params = new URLSearchParams(window.location.search);
    const productId = Number(params.get("id"));

    if (!productId) {
        showProductError();
        return;
    }

    const product = OnePunchData.getProductById(productId);

    if (!product) {
        showProductError();
        return;
    }

    renderProduct(product);
    renderStoreAvailability(product);
    configurePurchaseState(product);
}


/* =========================================================
   Product Rendering
   ========================================================= */

function renderProduct(product) {

    const category = OnePunchData.getCategoryById(
        product.categoryId
    );

    const image = document.querySelector("#product-image");
    const categoryElement = document.querySelector("#product-category");
    const nameElement = document.querySelector("#product-name");
    const franchiseElement = document.querySelector("#product-franchise");
    const descriptionElement = document.querySelector("#product-description");
    const priceElement = document.querySelector("#product-price");

    document.title =
        `${product.name} | One-Punch Anime Emporium`;

    image.src = product.image;
    image.alt = `${product.name} product image`;

    categoryElement.textContent =
        category ? category.name : product.categoryId;

    nameElement.textContent = product.name;

    franchiseElement.textContent =
        `Franchise: ${product.franchise}`;

    descriptionElement.textContent =
        product.description;

    priceElement.textContent =
        formatCurrency(product.price);
}


/* =========================================================
   Store Availability
   ========================================================= */

function renderStoreAvailability(product) {

    const container = document.querySelector(
        "#store-availability"
    );

    const records = OnePunchData.getInventoryForProduct(
        product.id
    );

    container.innerHTML = "";

    records.forEach(record => {

        const store = OnePunchData.getStoreById(
            record.storeId
        );

        if (!store) {
            return;
        }

        const card = document.createElement("article");

        card.className = "availability-card";

        const availabilityClass =
            getAvailabilityClass(
                record.availabilityStatus
            );

        card.innerHTML = `
            <h3>${escapeHtml(store.name)}</h3>

            <p class="store-address">
                ${escapeHtml(store.addressLine1)}<br>
                ${escapeHtml(store.city)},
                ${escapeHtml(store.state)}
                ${escapeHtml(store.postalCode)}
            </p>

            <p class="availability-badge ${availabilityClass}">
                ${escapeHtml(record.availabilityStatus)}
            </p>

            <p>
                ${getQuantityMessage(record)}
            </p>

            <a href="locations.html">
                Store Details →
            </a>
        `;

        container.appendChild(card);
    });
}


function getQuantityMessage(record) {

    if (record.quantityOnHand <= 0) {
        return "No demonstration inventory currently available.";
    }

    if (record.quantityOnHand === 1) {
        return "1 unit shown in demonstration inventory.";
    }

    return `${record.quantityOnHand} units shown in demonstration inventory.`;
}


/* =========================================================
   Purchase State
   ========================================================= */

function configurePurchaseState(product) {

    const overallAvailability =
        OnePunchData.getOverallAvailability(product.id);

    const availabilityElement =
        document.querySelector("#overall-availability");

    const purchaseActions =
        document.querySelector("#purchase-actions");

    const specialOrderSection =
        document.querySelector("#special-order-section");

    const specialOrderLink =
        document.querySelector("#special-order-link");

    availabilityElement.textContent =
        overallAvailability;

    availabilityElement.classList.add(
        getAvailabilityClass(overallAvailability)
    );

    const available =
        OnePunchData.isProductAvailable(product.id);

    if (!available) {

        purchaseActions.hidden = true;
        specialOrderSection.hidden = false;

        specialOrderLink.href =
            `special-orders.html?product=${encodeURIComponent(product.name)}&id=${product.id}`;

        return;
    }

    initializeAddToCart(product);
}


/* =========================================================
   Add to Cart
   ========================================================= */

function initializeAddToCart(product) {

    const button =
        document.querySelector("#add-to-cart");

    const quantitySelect =
        document.querySelector("#product-quantity");

    const message =
        document.querySelector("#cart-message");

    button.addEventListener("click", () => {

        const quantity =
            Number(quantitySelect.value);

        addProductToCart(
            product.id,
            quantity
        );

        message.textContent =
            `${product.name} added to cart.`;

        if (typeof updateCartCount === "function") {
            updateCartCount();
        }
    });
}


function addProductToCart(productId, quantity) {

    let cart = getCart();

    const existingItem =
        cart.find(
            item => item.productId === productId
        );

    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        cart.push({
            productId,
            quantity
        });
    }

    localStorage.setItem(
        "onePunchCart",
        JSON.stringify(cart)
    );
}


function getCart() {

    try {
        return JSON.parse(
            localStorage.getItem("onePunchCart")
        ) || [];
    } catch {
        return [];
    }
}


/* =========================================================
   Error State
   ========================================================= */

function showProductError() {

    const detail =
        document.querySelector("#product-detail");

    const availability =
        document.querySelector(
            "#store-availability"
        );

    const error =
        document.querySelector("#product-error");

    if (detail) {
        detail.hidden = true;
    }

    if (availability) {
        availability.closest("section").hidden = true;
    }

    if (error) {
        error.hidden = false;
    }
}


/* =========================================================
   Helpers
   ========================================================= */

function formatCurrency(value) {

    return new Intl.NumberFormat(
        "en-US",
        {
            style: "currency",
            currency: "USD"
        }
    ).format(value);
}


function getAvailabilityClass(status) {

    switch (status) {

        case "Available":
        case "In Stock":
            return "availability-in-stock";

        case "Limited Availability":
        case "Low Stock":
            return "availability-low-stock";

        default:
            return "availability-out-of-stock";
    }
}


function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}
