// Open the cart sidebar when cart icon is clicked
function openCart() {
    document.getElementById("cart-slidebar").style.right = "0px";  // Slide in the cart from the right
}

// Close the cart sidebar when close icon is clicked
function closeCart() {
    document.getElementById("cart-slidebar").style.right = "-300px";  // Hide the cart sidebar by sliding it out
}

// Toggle the cart visibility (alternative to openCart and closeCart)
function toggleCart() {
    var cartSidebar = document.getElementById("cart-slidebar");
    if (cartSidebar.style.right === "0px") {
        cartSidebar.style.right = "-300px";  // If cart is visible, hide it
    } else {
        cartSidebar.style.right = "0px";  // If cart is hidden, show it
    }
}

function toggleCategories() {
    var categoryItems = document.getElementById('category-items');
    
    // Toggle the display property (show/hide)
    if (categoryItems.style.display === "none") {
        categoryItems.style.display = "block";  // Show the categories
    } else {
        categoryItems.style.display = "none";  // Hide the categories
    }
}
