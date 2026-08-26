"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Shopping Cart
   ========================================================= */


const TAX_RATE = 0.065;


document.addEventListener("DOMContentLoaded", () => {
    renderCart();
    initializeCartControls();
});


/* =========================================================
   Cart Storage
   ========================================================= */

function getCart() {

    try {
        return JSON.parse(
            localStorage.getItem("onePunchCart")
        ) || [];
    } catch {
        return [];
    }
}


function saveCart(cart) {

    localStorage.setItem(
        "onePunchCart",
        JSON.stringify(cart)
    );

    if (typeof updateCartCount === "function") {
        updateCartCount();
    }
}


/* =========================================================
   Render Cart
   ========================================================= */

function renderCart() {

    const cart =
        getCart();

    const itemsContainer =
        document.querySelector("#cart-items");

    const emptyCart =
        document.querySelector("#empty-cart");

    const cartSummary =
        document.querySelector("#cart-summary");

    itemsContainer.innerHTML = "";


    if (cart.length === 0) {

        emptyCart.hidden = false;
        cartSummary.hidden = true;

        updateCartSummary([]);

        return;
    }


    emptyCart.hidden = true;
    cartSummary.hidden = false;


    cart.forEach(item => {

        const product =
            OnePunchData.getProductById(
                item.productId
            );

        if (!product) {
            return;
        }

        itemsContainer.appendChild(
            createCartItem(
                product,
                item.quantity
            )
        );
    });


    updateCartSummary(cart);
}


/* =========================================================
   Create Item
   ========================================================= */

function createCartItem(product, quantity) {

    const item =
        document.createElement("article");

    item.className =
        "cart-item";

    const lineTotal =
        product.price * quantity;


    item.innerHTML = `

        <a
            class="cart-item-image"
            href="product.html?id=${product.id}"
        >
            <img
                src="${escapeHtml(product.image)}"
                alt="${escapeHtml(product.name)}"
            >
        </a>

        <div class="cart-item-content">

            <div>

                <p class="cart-item-category">
                    ${escapeHtml(
                        getCategoryName(product.categoryId)
                    )}
                </p>

                <h2>
                    <a href="product.html?id=${product.id}">
                        ${escapeHtml(product.name)}
                    </a>
                </h2>

                <p class="cart-item-franchise">
                    ${escapeHtml(product.franchise)}
                </p>

                <p class="cart-item-price">
                    ${formatCurrency(product.price)} each
                </p>

            </div>


            <div class="cart-item-controls">

                <label
                    for="quantity-${product.id}"
                >
                    Quantity
                </label>

                <select
                    id="quantity-${product.id}"
                    class="cart-quantity"
                    data-product-id="${product.id}"
                >
                    ${buildQuantityOptions(quantity)}
                </select>

                <button
                    class="cart-remove"
                    type="button"
                    data-product-id="${product.id}"
                >
                    Remove
                </button>

            </div>

        </div>


        <div class="cart-item-total">

            <p>Item Total</p>

            <strong>
                ${formatCurrency(lineTotal)}
            </strong>

        </div>
    `;

    return item;
}


/* =========================================================
   Controls
   ========================================================= */

function initializeCartControls() {

    const container =
        document.querySelector("#cart-items");

    const clearButton =
        document.querySelector("#clear-cart");


    container.addEventListener(
        "change",
        event => {

            if (
                event.target.classList.contains(
                    "cart-quantity"
                )
            ) {

                updateItemQuantity(
                    Number(
                        event.target.dataset.productId
                    ),
                    Number(
                        event.target.value
                    )
                );

            }
        }
    );


    container.addEventListener(
        "click",
        event => {

            if (
                event.target.classList.contains(
                    "cart-remove"
                )
            ) {

                removeItem(
                    Number(
                        event.target.dataset.productId
                    )
                );

            }
        }
    );


    clearButton.addEventListener(
        "click",
        clearCart
    );
}


/* =========================================================
   Quantity
   ========================================================= */

function updateItemQuantity(
    productId,
    quantity
) {

    const cart =
        getCart();

    const item =
        cart.find(
            item =>
                item.productId === productId
        );


    if (!item) {
        return;
    }


    item.quantity = quantity;

    saveCart(cart);
    renderCart();
}


/* =========================================================
   Remove
   ========================================================= */

function removeItem(productId) {

    const cart =
        getCart().filter(
            item =>
                item.productId !== productId
        );

    saveCart(cart);
    renderCart();
}


/* =========================================================
   Clear
   ========================================================= */

function clearCart() {

    localStorage.removeItem(
        "onePunchCart"
    );

    if (
        typeof updateCartCount ===
        "function"
    ) {
        updateCartCount();
    }

    renderCart();
}


/* =========================================================
   Summary
   ========================================================= */

function updateCartSummary(cart) {

    let subtotal = 0;
    let itemCount = 0;


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

        itemCount +=
            item.quantity;
    });


    const tax =
        subtotal * TAX_RATE;

    const total =
        subtotal + tax;


    document.querySelector(
        "#summary-item-count"
    ).textContent =
        itemCount;


    document.querySelector(
        "#summary-subtotal"
    ).textContent =
        formatCurrency(subtotal);


    document.querySelector(
        "#summary-tax"
    ).textContent =
        formatCurrency(tax);


    document.querySelector(
        "#summary-total"
    ).textContent =
        formatCurrency(total);
}


/* =========================================================
   Helpers
   ========================================================= */

function getCategoryName(categoryId) {

    const category =
        OnePunchData.getCategoryById(
            categoryId
        );

    return category
        ? category.name
        : categoryId;
}


function buildQuantityOptions(
    selectedQuantity
) {

    let options = "";


    for (
        let quantity = 1;
        quantity <= 10;
        quantity++
    ) {

        options += `
            <option
                value="${quantity}"
                ${
                    quantity ===
                    selectedQuantity
                        ? "selected"
                        : ""
                }
            >
                ${quantity}
            </option>
        `;
    }


    return options;
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
