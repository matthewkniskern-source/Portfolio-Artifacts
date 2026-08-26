"use strict";

/* =========================================================
   One-Punch Anime Emporium
   Demonstration Data

   Academic / portfolio prototype only.

   Data is intentionally separated into:
   - categories
   - stores
   - products
   - inventory

   Inventory follows the relationship:

       Store + Product -> Inventory

   No data in this file represents live retail inventory.
   ========================================================= */


/* =========================================================
   Categories
   ========================================================= */

const categories = [
    {
        id: "manga",
        name: "Manga",
        description: "Manga volumes, omnibus editions, and collected series."
    },
    {
        id: "figures",
        name: "Figures",
        description: "Character figures, statues, and display collectibles."
    },
    {
        id: "collectibles",
        name: "Collectibles",
        description: "Trading items, display pieces, pins, and specialty merchandise."
    },
    {
        id: "apparel",
        name: "Apparel",
        description: "Shirts, hoodies, hats, and other anime-inspired clothing."
    },
    {
        id: "accessories",
        name: "Accessories",
        description: "Bags, wallets, keychains, desk items, and everyday gear."
    },
    {
        id: "comics",
        name: "Comics",
        description: "American comics, graphic novels, and collected editions."
    }
];


/* =========================================================
   Stores

   Academic scenario:
   Primary retail store + 3 additional locations = 4 stores.

   Addresses are fictional demonstration data.
   ========================================================= */

const stores = [
    {
        id: "store01",
        name: "Downtown Chico",
        displayName: "One-Punch Anime Emporium - Downtown Chico",
        addressLine1: "101 Hero Avenue",
        city: "Chico",
        state: "CA",
        postalCode: "95928",
        phone: "(530) 555-0101",
        hours: {
            mondayThursday: "10:00 AM - 8:00 PM",
            fridaySaturday: "10:00 AM - 9:00 PM",
            sunday: "11:00 AM - 6:00 PM"
        }
    },
    {
        id: "store02",
        name: "North Chico",
        displayName: "One-Punch Anime Emporium - North Chico",
        addressLine1: "225 Titan Boulevard",
        city: "Chico",
        state: "CA",
        postalCode: "95926",
        phone: "(530) 555-0102",
        hours: {
            mondayThursday: "10:00 AM - 8:00 PM",
            fridaySaturday: "10:00 AM - 9:00 PM",
            sunday: "11:00 AM - 6:00 PM"
        }
    },
    {
        id: "store03",
        name: "East Chico",
        displayName: "One-Punch Anime Emporium - East Chico",
        addressLine1: "88 Shonen Street",
        city: "Chico",
        state: "CA",
        postalCode: "95973",
        phone: "(530) 555-0103",
        hours: {
            mondayThursday: "10:00 AM - 8:00 PM",
            fridaySaturday: "10:00 AM - 9:00 PM",
            sunday: "11:00 AM - 6:00 PM"
        }
    },
    {
        id: "store04",
        name: "South Chico",
        displayName: "One-Punch Anime Emporium - South Chico",
        addressLine1: "404 Capsule Drive",
        city: "Chico",
        state: "CA",
        postalCode: "95928",
        phone: "(530) 555-0104",
        hours: {
            mondayThursday: "10:00 AM - 8:00 PM",
            fridaySaturday: "10:00 AM - 9:00 PM",
            sunday: "11:00 AM - 6:00 PM"
        }
    }
];


/* =========================================================
   Products
   36 products
   6 categories
   6 products per category
   ========================================================= */

const products = [

    /* -----------------------------------------------------
       Manga
       ----------------------------------------------------- */

    {
        id: 1001,
        sku: "MNG-001",
        name: "One-Punch Man Vol. 1",
        categoryId: "manga",
        franchise: "One-Punch Man",
        price: 11.99,
        image: "assets/images/products/manga-01.jpg",
        description: "The opening volume of the superhero comedy following Saitama and his search for a worthy opponent.",
        keywords: ["saitama", "genos", "hero", "shonen", "manga"],
        featured: true
    },
    {
        id: 1002,
        sku: "MNG-002",
        name: "Chainsaw Man Vol. 1",
        categoryId: "manga",
        franchise: "Chainsaw Man",
        price: 11.99,
        image: "assets/images/products/manga-02.jpg",
        description: "The first volume of the dark action series following Denji and his transformation into Chainsaw Man.",
        keywords: ["denji", "pochita", "devil", "shonen", "manga"],
        featured: false
    },
    {
        id: 1003,
        sku: "MNG-003",
        name: "Spy x Family Vol. 1",
        categoryId: "manga",
        franchise: "Spy x Family",
        price: 11.99,
        image: "assets/images/products/manga-03.jpg",
        description: "Loid Forger assembles an unconventional family for a mission where everyone is hiding something.",
        keywords: ["loid", "anya", "yor", "forger", "manga"],
        featured: true
    },
    {
        id: 1004,
        sku: "MNG-004",
        name: "Jujutsu Kaisen Vol. 1",
        categoryId: "manga",
        franchise: "Jujutsu Kaisen",
        price: 11.99,
        image: "assets/images/products/manga-04.jpg",
        description: "Yuji Itadori enters the dangerous world of curses after encountering a powerful cursed object.",
        keywords: ["yuji", "gojo", "sukuna", "curse", "manga"],
        featured: false
    },
    {
        id: 1005,
        sku: "MNG-005",
        name: "Demon Slayer Vol. 1",
        categoryId: "manga",
        franchise: "Demon Slayer",
        price: 11.99,
        image: "assets/images/products/manga-05.jpg",
        description: "Tanjiro begins his journey as a demon slayer after tragedy strikes his family.",
        keywords: ["tanjiro", "nezuko", "demon", "slayer", "manga"],
        featured: false
    },
    {
        id: 1006,
        sku: "MNG-006",
        name: "My Hero Academia Vol. 1",
        categoryId: "manga",
        franchise: "My Hero Academia",
        price: 11.99,
        image: "assets/images/products/manga-06.jpg",
        description: "Izuku Midoriya begins his path toward becoming a hero in a world where superpowers are the norm.",
        keywords: ["deku", "midoriya", "all might", "hero", "manga"],
        featured: false
    },


    /* -----------------------------------------------------
       Figures
       ----------------------------------------------------- */

    {
        id: 1007,
        sku: "FIG-001",
        name: "Saitama Hero Figure",
        categoryId: "figures",
        franchise: "One-Punch Man",
        price: 34.99,
        image: "assets/images/products/figure-01.jpg",
        description: "Display figure featuring Saitama in his classic hero costume.",
        keywords: ["saitama", "one punch man", "hero", "figure"],
        featured: true
    },
    {
        id: 1008,
        sku: "FIG-002",
        name: "Gojo Satoru Display Figure",
        categoryId: "figures",
        franchise: "Jujutsu Kaisen",
        price: 42.99,
        image: "assets/images/products/figure-02.jpg",
        description: "Detailed display figure featuring Gojo Satoru.",
        keywords: ["gojo", "jujutsu kaisen", "satoru", "figure"],
        featured: true
    },
    {
        id: 1009,
        sku: "FIG-003",
        name: "Anya Forger Mini Figure",
        categoryId: "figures",
        franchise: "Spy x Family",
        price: 24.99,
        image: "assets/images/products/figure-03.jpg",
        description: "Compact Anya Forger figure designed for desks and smaller displays.",
        keywords: ["anya", "spy x family", "forger", "figure"],
        featured: false
    },
    {
        id: 1010,
        sku: "FIG-004",
        name: "Tanjiro Kamado Battle Figure",
        categoryId: "figures",
        franchise: "Demon Slayer",
        price: 44.99,
        image: "assets/images/products/figure-04.jpg",
        description: "Action pose figure inspired by Tanjiro Kamado's sword techniques.",
        keywords: ["tanjiro", "demon slayer", "kamado", "figure"],
        featured: false
    },
    {
        id: 1011,
        sku: "FIG-005",
        name: "Power Display Figure",
        categoryId: "figures",
        franchise: "Chainsaw Man",
        price: 39.99,
        image: "assets/images/products/figure-05.jpg",
        description: "Display figure featuring Power from Chainsaw Man.",
        keywords: ["power", "chainsaw man", "devil", "figure"],
        featured: false
    },
    {
        id: 1012,
        sku: "FIG-006",
        name: "All Might Hero Figure",
        categoryId: "figures",
        franchise: "My Hero Academia",
        price: 46.99,
        image: "assets/images/products/figure-06.jpg",
        description: "Large-format display figure featuring the Symbol of Peace.",
        keywords: ["all might", "my hero academia", "hero", "figure"],
        featured: false
    },


    /* -----------------------------------------------------
       Collectibles
       ----------------------------------------------------- */

    {
        id: 1013,
        sku: "COL-001",
        name: "Hero Association Enamel Pin Set",
        categoryId: "collectibles",
        franchise: "One-Punch Man",
        price: 18.99,
        image: "assets/images/products/collectible-01.jpg",
        description: "Four-piece enamel pin set inspired by the Hero Association.",
        keywords: ["hero association", "pins", "saitama", "collectible"],
        featured: false
    },
    {
        id: 1014,
        sku: "COL-002",
        name: "Jujutsu High Badge Collection",
        categoryId: "collectibles",
        franchise: "Jujutsu Kaisen",
        price: 16.99,
        image: "assets/images/products/collectible-02.jpg",
        description: "Collectible badge set inspired by Tokyo Jujutsu High.",
        keywords: ["jujutsu high", "badge", "gojo", "collectible"],
        featured: false
    },
    {
        id: 1015,
        sku: "COL-003",
        name: "Survey Corps Insignia Replica",
        categoryId: "collectibles",
        franchise: "Attack on Titan",
        price: 27.99,
        image: "assets/images/products/collectible-03.jpg",
        description: "Decorative replica inspired by the Survey Corps insignia.",
        keywords: ["attack on titan", "survey corps", "insignia", "collectible"],
        featured: true
    },
    {
        id: 1016,
        sku: "COL-004",
        name: "Capsule Corp Desk Replica",
        categoryId: "collectibles",
        franchise: "Dragon Ball",
        price: 29.99,
        image: "assets/images/products/collectible-04.jpg",
        description: "Small display piece inspired by Capsule Corporation technology.",
        keywords: ["dragon ball", "capsule corp", "bulma", "collectible"],
        featured: false
    },
    {
        id: 1017,
        sku: "COL-005",
        name: "Straw Hat Crew Wanted Poster Set",
        categoryId: "collectibles",
        franchise: "One Piece",
        price: 21.99,
        image: "assets/images/products/collectible-05.jpg",
        description: "Decorative wanted-poster set featuring members of the Straw Hat crew.",
        keywords: ["one piece", "luffy", "straw hat", "poster", "collectible"],
        featured: false
    },
    {
        id: 1018,
        sku: "COL-006",
        name: "Akatsuki Cloud Display Set",
        categoryId: "collectibles",
        franchise: "Naruto",
        price: 19.99,
        image: "assets/images/products/collectible-06.jpg",
        description: "Desktop display pieces inspired by the Akatsuki cloud emblem.",
        keywords: ["naruto", "akatsuki", "cloud", "collectible"],
        featured: false
    },


    /* -----------------------------------------------------
       Apparel
       ----------------------------------------------------- */

    {
        id: 1019,
        sku: "APP-001",
        name: "One-Punch Hero Training Shirt",
        categoryId: "apparel",
        franchise: "One-Punch Man",
        price: 24.99,
        image: "assets/images/products/apparel-01.jpg",
        description: "Graphic tee inspired by Saitama's famously straightforward training routine.",
        keywords: ["saitama", "shirt", "training", "apparel"],
        featured: true
    },
    {
        id: 1020,
        sku: "APP-002",
        name: "Jujutsu High Hoodie",
        categoryId: "apparel",
        franchise: "Jujutsu Kaisen",
        price: 54.99,
        image: "assets/images/products/apparel-02.jpg",
        description: "Pullover hoodie inspired by Tokyo Jujutsu High.",
        keywords: ["jujutsu kaisen", "hoodie", "gojo", "apparel"],
        featured: false
    },
    {
        id: 1021,
        sku: "APP-003",
        name: "Survey Corps Green Hoodie",
        categoryId: "apparel",
        franchise: "Attack on Titan",
        price: 59.99,
        image: "assets/images/products/apparel-03.jpg",
        description: "Green pullover hoodie featuring Survey Corps-inspired graphics.",
        keywords: ["attack on titan", "survey corps", "hoodie", "apparel"],
        featured: false
    },
    {
        id: 1022,
        sku: "APP-004",
        name: "Straw Hat Pirate Tee",
        categoryId: "apparel",
        franchise: "One Piece",
        price: 26.99,
        image: "assets/images/products/apparel-04.jpg",
        description: "Casual graphic tee inspired by the Straw Hat Pirates.",
        keywords: ["one piece", "luffy", "shirt", "pirate", "apparel"],
        featured: false
    },
    {
        id: 1023,
        sku: "APP-005",
        name: "U.A. Academy Training Shirt",
        categoryId: "apparel",
        franchise: "My Hero Academia",
        price: 25.99,
        image: "assets/images/products/apparel-05.jpg",
        description: "Training-style shirt inspired by U.A. High School.",
        keywords: ["my hero academia", "ua", "deku", "shirt", "apparel"],
        featured: false
    },
    {
        id: 1024,
        sku: "APP-006",
        name: "Demon Slayer Corps Cap",
        categoryId: "apparel",
        franchise: "Demon Slayer",
        price: 22.99,
        image: "assets/images/products/apparel-06.jpg",
        description: "Adjustable cap featuring Demon Slayer Corps-inspired embroidery.",
        keywords: ["demon slayer", "cap", "hat", "apparel"],
        featured: false
    },


    /* -----------------------------------------------------
       Accessories
       ----------------------------------------------------- */

    {
        id: 1025,
        sku: "ACC-001",
        name: "Saitama Grocery Tote",
        categoryId: "accessories",
        franchise: "One-Punch Man",
        price: 14.99,
        image: "assets/images/products/accessory-01.jpg",
        description: "Reusable tote inspired by Saitama's dedication to supermarket sale day.",
        keywords: ["saitama", "tote", "bag", "accessory"],
        featured: false
    },
    {
        id: 1026,
        sku: "ACC-002",
        name: "Anya Forger School Bag",
        categoryId: "accessories",
        franchise: "Spy x Family",
        price: 39.99,
        image: "assets/images/products/accessory-02.jpg",
        description: "Compact shoulder bag featuring Anya-inspired design details.",
        keywords: ["anya", "spy x family", "bag", "accessory"],
        featured: true
    },
    {
        id: 1027,
        sku: "ACC-003",
        name: "Akatsuki Cloud Wallet",
        categoryId: "accessories",
        franchise: "Naruto",
        price: 21.99,
        image: "assets/images/products/accessory-03.jpg",
        description: "Bifold wallet with an Akatsuki-inspired cloud pattern.",
        keywords: ["naruto", "akatsuki", "wallet", "accessory"],
        featured: false
    },
    {
        id: 1028,
        sku: "ACC-004",
        name: "Dragon Radar Keychain",
        categoryId: "accessories",
        franchise: "Dragon Ball",
        price: 12.99,
        image: "assets/images/products/accessory-04.jpg",
        description: "Keychain inspired by Bulma's Dragon Radar.",
        keywords: ["dragon ball", "dragon radar", "keychain", "accessory"],
        featured: false
    },
    {
        id: 1029,
        sku: "ACC-005",
        name: "Demon Slayer Sword Keychain Set",
        categoryId: "accessories",
        franchise: "Demon Slayer",
        price: 17.99,
        image: "assets/images/products/accessory-05.jpg",
        description: "Miniature decorative keychain set inspired by Nichirin sword designs.",
        keywords: ["demon slayer", "nichirin", "keychain", "accessory"],
        featured: false
    },
    {
        id: 1030,
        sku: "ACC-006",
        name: "Straw Hat Crew Lanyard",
        categoryId: "accessories",
        franchise: "One Piece",
        price: 11.99,
        image: "assets/images/products/accessory-06.jpg",
        description: "Printed lanyard featuring Straw Hat crew-inspired artwork.",
        keywords: ["one piece", "straw hat", "lanyard", "accessory"],
        featured: false
    },


    /* -----------------------------------------------------
       Comics
       ----------------------------------------------------- */

    {
        id: 1031,
        sku: "COM-001",
        name: "Batman: Year One",
        categoryId: "comics",
        franchise: "Batman",
        price: 16.99,
        image: "assets/images/products/comic-01.jpg",
        description: "Collected graphic novel chronicling an early chapter in Batman's career.",
        keywords: ["batman", "dc", "gotham", "graphic novel", "comic"],
        featured: true
    },
    {
        id: 1032,
        sku: "COM-002",
        name: "Spider-Man: Blue",
        categoryId: "comics",
        franchise: "Spider-Man",
        price: 19.99,
        image: "assets/images/products/comic-02.jpg",
        description: "Collected Spider-Man story centered on memory, loss, and Peter Parker's early years.",
        keywords: ["spider-man", "marvel", "peter parker", "graphic novel", "comic"],
        featured: false
    },
    {
        id: 1033,
        sku: "COM-003",
        name: "Superman: For All Seasons",
        categoryId: "comics",
        franchise: "Superman",
        price: 19.99,
        image: "assets/images/products/comic-03.jpg",
        description: "A character-driven Superman story told through the people and places that shaped him.",
        keywords: ["superman", "dc", "clark kent", "graphic novel", "comic"],
        featured: false
    },
    {
        id: 1034,
        sku: "COM-004",
        name: "Ms. Marvel: No Normal",
        categoryId: "comics",
        franchise: "Ms. Marvel",
        price: 15.99,
        image: "assets/images/products/comic-04.jpg",
        description: "Collected introduction to Kamala Khan as she discovers her powers and identity.",
        keywords: ["ms marvel", "kamala khan", "marvel", "graphic novel", "comic"],
        featured: false
    },
    {
        id: 1035,
        sku: "COM-005",
        name: "Teenage Mutant Ninja Turtles Collection",
        categoryId: "comics",
        franchise: "Teenage Mutant Ninja Turtles",
        price: 24.99,
        image: "assets/images/products/comic-05.jpg",
        description: "Collected adventures featuring the Teenage Mutant Ninja Turtles.",
        keywords: ["tmnt", "turtles", "comic", "graphic novel"],
        featured: false
    },
    {
        id: 1036,
        sku: "COM-006",
        name: "Invincible Vol. 1",
        categoryId: "comics",
        franchise: "Invincible",
        price: 14.99,
        image: "assets/images/products/comic-06.jpg",
        description: "The opening collected volume following Mark Grayson as his superhero abilities emerge.",
        keywords: ["invincible", "mark grayson", "superhero", "comic"],
        featured: true
    }
];


/* =========================================================
   Inventory Matrix

   Each product maps to inventory at all four stores.

   Format:

   ProductID: [Downtown, Northside, Eastgate, Lakeside]

   This compact structure is expanded below into individual
   Store + Product inventory records.

   Inventory deliberately includes:
   - broadly available products
   - low stock
   - single-store availability
   - two-store availability
   - fully out-of-stock products
   ========================================================= */

const inventoryMatrix = {

    /* Manga */
    1001: [7, 5, 3, 6],
    1002: [4, 0, 2, 5],
    1003: [8, 6, 7, 3],
    1004: [2, 1, 0, 4],
    1005: [0, 0, 3, 2],
    1006: [0, 0, 0, 0],

    /* Figures */
    1007: [3, 1, 0, 2],
    1008: [1, 0, 0, 0],
    1009: [5, 3, 4, 2],
    1010: [0, 2, 0, 1],
    1011: [2, 0, 1, 0],
    1012: [0, 0, 0, 0],

    /* Collectibles */
    1013: [8, 5, 6, 7],
    1014: [3, 2, 0, 4],
    1015: [0, 1, 0, 0],
    1016: [2, 2, 2, 2],
    1017: [5, 0, 4, 3],
    1018: [0, 0, 0, 0],

    /* Apparel */
    1019: [10, 7, 8, 6],
    1020: [3, 0, 1, 2],
    1021: [0, 2, 0, 0],
    1022: [4, 5, 3, 4],
    1023: [2, 1, 0, 3],
    1024: [0, 0, 2, 0],

    /* Accessories */
    1025: [9, 6, 8, 7],
    1026: [1, 0, 2, 0],
    1027: [4, 3, 0, 2],
    1028: [6, 5, 4, 5],
    1029: [0, 2, 1, 0],
    1030: [0, 0, 0, 0],

    /* Comics */
    1031: [4, 3, 2, 5],
    1032: [2, 0, 1, 2],
    1033: [0, 1, 0, 0],
    1034: [3, 2, 2, 0],
    1035: [1, 0, 0, 1],
    1036: [0, 0, 0, 0]
};


/* =========================================================
   Inventory Status Logic

   This is demonstration logic only.

   0      -> Out of Stock
   1-2    -> Low Stock
   3+     -> In Stock
   ========================================================= */

function getAvailabilityStatus(quantity) {
    if (quantity <= 0) {
        return "Out of Stock";
    }

    if (quantity <= 2) {
        return "Low Stock";
    }

    return "In Stock";
}


/* =========================================================
   Build Separate Inventory Dataset

   Output example:

   {
       id: "INV-1001-store01",
       productId: 1001,
       storeId: "store01",
       quantityOnHand: 7,
       quantityReserved: 0,
       availabilityStatus: "In Stock"
   }
   ========================================================= */

const inventory = [];

Object.entries(inventoryMatrix).forEach(([productId, quantities]) => {

    stores.forEach((store, index) => {

        const quantity = quantities[index] ?? 0;

        inventory.push({
            id: `INV-${productId}-${store.id}`,
            productId: Number(productId),
            storeId: store.id,
            quantityOnHand: quantity,
            quantityReserved: 0,
            availabilityStatus: getAvailabilityStatus(quantity)
        });

    });

});


/* =========================================================
   Data Helper Functions
   ========================================================= */


/**
 * Return a single product by numeric ID.
 */
function getProductById(productId) {
    return products.find(
        product => product.id === Number(productId)
    ) || null;
}


/**
 * Return a category by ID.
 */
function getCategoryById(categoryId) {
    return categories.find(
        category => category.id === categoryId
    ) || null;
}


/**
 * Return a store by ID.
 */
function getStoreById(storeId) {
    return stores.find(
        store => store.id === storeId
    ) || null;
}


/**
 * Return every inventory record for a product.
 */
function getInventoryForProduct(productId) {
    return inventory.filter(
        record => record.productId === Number(productId)
    );
}


/**
 * Return every inventory record for a store.
 */
function getInventoryForStore(storeId) {
    return inventory.filter(
        record => record.storeId === storeId
    );
}


/**
 * Return the inventory record for one product at one store.
 */
function getInventoryRecord(productId, storeId) {
    return inventory.find(
        record =>
            record.productId === Number(productId) &&
            record.storeId === storeId
    ) || null;
}


/**
 * Return total on-hand quantity across all stores.
 */
function getTotalInventory(productId) {
    return getInventoryForProduct(productId)
        .reduce(
            (total, record) => total + record.quantityOnHand,
            0
        );
}


/**
 * Return true when product exists at any store.
 */
function isProductAvailable(productId) {
    return getTotalInventory(productId) > 0;
}


/**
 * Return customer-facing overall availability.
 */
function getOverallAvailability(productId) {

    const total = getTotalInventory(productId);

    if (total === 0) {
        return "Out of Stock";
    }

    if (total <= 4) {
        return "Limited Availability";
    }

    return "Available";
}


/**
 * Search products across common customer-facing fields.
 */
function searchProducts(searchTerm) {

    const term = String(searchTerm || "")
        .trim()
        .toLowerCase();

    if (!term) {
        return [...products];
    }

    return products.filter(product => {

        const searchableText = [
            product.name,
            product.franchise,
            product.categoryId,
            product.description,
            ...product.keywords
        ]
            .join(" ")
            .toLowerCase();

        return searchableText.includes(term);

    });
}


/**
 * Return products in one category.
 */
function getProductsByCategory(categoryId) {

    if (!categoryId) {
        return [...products];
    }

    return products.filter(
        product => product.categoryId === categoryId
    );
}


/**
 * Return products currently available at any store.
 */
function getAvailableProducts() {
    return products.filter(
        product => isProductAvailable(product.id)
    );
}


/**
 * Return products currently sold out at all stores.
 */
function getOutOfStockProducts() {
    return products.filter(
        product => !isProductAvailable(product.id)
    );
}


/**
 * Return products marked for home-page or promotional use.
 */
function getFeaturedProducts() {
    return products.filter(
        product => product.featured === true
    );
}


/* =========================================================
   Expose Demonstration Data

   The site uses ordinary script tags rather than modules
   so GitHub Pages can serve the prototype without a build
   process.

   Other scripts can access:

       OnePunchData.products
       OnePunchData.stores
       OnePunchData.inventory
       OnePunchData.getProductById(...)
       etc.
   ========================================================= */

window.OnePunchData = {

    categories,
    stores,
    products,
    inventory,

    getAvailabilityStatus,
    getProductById,
    getCategoryById,
    getStoreById,
    getInventoryForProduct,
    getInventoryForStore,
    getInventoryRecord,
    getTotalInventory,
    isProductAvailable,
    getOverallAvailability,
    searchProducts,
    getProductsByCategory,
    getAvailableProducts,
    getOutOfStockProducts,
    getFeaturedProducts

};
