"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Product Catalog Page
   ========================================================= */


document.addEventListener("DOMContentLoaded", () => {
    initializeCatalog();
});


function initializeCatalog() {

    populateCategoryFilter();
    loadCategoryFromQueryString();
    attachCatalogEvents();
    renderCatalog();
}


/* =========================================================
   Category Filter
   ========================================================= */

function populateCategoryFilter() {

    const categoryFilter =
        document.querySelector("#category-filter");

    if (!categoryFilter) {
        return;
    }

    OnePunchData.categories.forEach(category => {

        const option =
            document.createElement("option");

        option.value = category.id;
        option.textContent = category.name;

        categoryFilter.appendChild(option);
    });
}


function loadCategoryFromQueryString() {

    const params =
        new URLSearchParams(window.location.search);

    const requestedCategory =
        params.get("category");

    if (!requestedCategory) {
        return;
    }

    const categoryFilter =
        document.querySelector("#category-filter");

    const matchingCategory =
        OnePunchData.categories.find(category =>
            category.id.toLowerCase() ===
                requestedCategory.toLowerCase() ||
            category.name.toLowerCase() ===
                requestedCategory.toLowerCase()
        );

    if (matchingCategory) {
        categoryFilter.value =
            matchingCategory.id;
    }
}


/* =========================================================
   Events
   ========================================================= */

function attachCatalogEvents() {

    const searchInput =
        document.querySelector("#product-search");

    const categoryFilter =
        document.querySelector("#category-filter");

    const availabilityFilter =
        document.querySelector("#availability-filter");

    const resetButton =
        document.querySelector("#reset-filters");

    const noResultsReset =
        document.querySelector("#no-results-reset");


    searchInput.addEventListener(
        "input",
        renderCatalog
    );

    categoryFilter.addEventListener(
        "change",
        renderCatalog
    );

    availabilityFilter.addEventListener(
        "change",
        renderCatalog
    );

    resetButton.addEventListener(
        "click",
        resetFilters
    );

    noResultsReset.addEventListener(
        "click",
        resetFilters
    );
}


/* =========================================================
   Filtering
   ========================================================= */

function getFilteredProducts() {

    const searchTerm =
        document.querySelector("#product-search")
            .value
            .trim()
            .toLowerCase();

    const categoryId =
        document.querySelector("#category-filter")
            .value;

    const availability =
        document.querySelector("#availability-filter")
            .value;


    return OnePunchData.products.filter(product => {

        const matchesSearch =
            matchesSearchTerm(
                product,
                searchTerm
            );

        const matchesCategory =
            !categoryId ||
            product.categoryId === categoryId;

        const matchesAvailability =
            matchesAvailabilityFilter(
                product,
                availability
            );

        return (
            matchesSearch &&
            matchesCategory &&
            matchesAvailability
        );
    });
}


function matchesSearchTerm(product, searchTerm) {

    if (!searchTerm) {
        return true;
    }

    const category =
        OnePunchData.getCategoryById(
            product.categoryId
        );

    const searchableText = [
        product.name,
        product.franchise,
        product.description,
        product.sku,
        category ? category.name : "",
        ...product.keywords
    ]
        .join(" ")
        .toLowerCase();

    return searchableText.includes(
        searchTerm
    );
}


function matchesAvailabilityFilter(
    product,
    filter
) {

    if (!filter) {
        return true;
    }

    const status =
        OnePunchData.getOverallAvailability(
            product.id
        );

    if (filter === "available") {
        return status === "Available";
    }

    if (filter === "limited") {
        return status ===
            "Limited Availability";
    }

    if (filter === "out") {
        return status ===
            "Out of Stock";
    }

    return true;
}


/* =========================================================
   Rendering
   ========================================================= */

function renderCatalog() {

    const grid =
        document.querySelector("#product-grid");

    const noResults =
        document.querySelector("#no-results");

    const products =
        getFilteredProducts();

    grid.innerHTML = "";

    if (products.length === 0) {

        noResults.hidden = false;
        updateResultsCount(0);

        return;
    }

    noResults.hidden = true;

    products.forEach(product => {
        grid.appendChild(
            createProductCard(product)
        );
    });

    updateResultsCount(
        products.length
    );
}


function createProductCard(product) {

    const category =
        OnePunchData.getCategoryById(
            product.categoryId
        );

    const status =
        OnePunchData.getOverallAvailability(
            product.id
        );

    const card =
        document.createElement("article");

    card.className =
        "product-card";

    const availabilityClass =
        getAvailabilityClass(status);

    card.innerHTML = `

  <a
    class="product-card-image"
    href="product.html?id=${product.id}"
    aria-label="View ${escapeHtml(product.name)}"
>
    <img
        src="/.netlify/images?url=${encodeURIComponent(product.image)}&w=400&q=75"
        srcset="
            /.netlify/images?url=${encodeURIComponent(product.image)}&w=300&q=75 300w,
            /.netlify/images?url=${encodeURIComponent(product.image)}&w=500&q=75 500w,
            /.netlify/images?url=${encodeURIComponent(product.image)}&w=700&q=75 700w
        "
        sizes="
            (max-width: 600px) 100vw,
            (max-width: 900px) 50vw,
            25vw
        "
        loading="lazy"
        decoding="async"
        alt="${escapeHtml(product.name)}"
    >
</a>

        <div class="product-card-content">

            <p class="product-card-category">
                ${escapeHtml(
                    category
                        ? category.name
                        : product.categoryId
                )}
            </p>

            <h2>
                <a href="product.html?id=${product.id}">
                    ${escapeHtml(product.name)}
                </a>
            </h2>

            <p class="product-card-franchise">
                ${escapeHtml(product.franchise)}
            </p>

            <div class="product-card-footer">

                <p class="product-card-price">
                    ${formatCurrency(product.price)}
                </p>

                <p
                    class="availability-badge ${availabilityClass}"
                >
                    ${escapeHtml(status)}
                </p>

            </div>

        </div>
    `;

    return card;
}


/* =========================================================
   Results
   ========================================================= */

function updateResultsCount(count) {

    const countElement =
        document.querySelector(
            "#results-count"
        );

    countElement.textContent =
        `${count} product${count === 1 ? "" : "s"} shown`;
}


/* =========================================================
   Reset
   ========================================================= */

function resetFilters() {

    document.querySelector(
        "#product-search"
    ).value = "";

    document.querySelector(
        "#category-filter"
    ).value = "";

    document.querySelector(
        "#availability-filter"
    ).value = "";

    const cleanUrl =
        window.location.pathname;

    window.history.replaceState(
        {},
        "",
        cleanUrl
    );

    renderCatalog();
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
            return "availability-in-stock";

        case "Limited Availability":
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

