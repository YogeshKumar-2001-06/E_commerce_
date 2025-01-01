
document.addEventListener("DOMContentLoaded", function() {
    // Select all elements with the class 'stars'
    const starElements = document.querySelectorAll('.stars');
    
    starElements.forEach(function(starElement) {
        const rating = parseInt(starElement.getAttribute('data-rating'), 10); // Get rating value
        
        let stars = '';
        
        // Generate filled stars (⭐) and empty stars (☆)
        for (let i = 1; i <= 5; i++) {
            if (i <= rating) {
                stars += '⭐'; // Filled star
            } else {
                stars += '☆'; // Empty star
            }
        }
        
        // Set the inner HTML of the star element to the generated stars
        starElement.innerHTML = stars;
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".tab");
    const sections = document.querySelectorAll(".details-section");
    const form = document.querySelector(".form");
    const addressList = document.getElementById("address-list");
    const addAddressBtn = document.getElementById("add-address-btn");

    // Handle tab switching
    tabs.forEach((tab, index) => {
        tab.addEventListener("click", () => {
            tabs.forEach(t => t.classList.remove("active"));
            tab.classList.add("active");

            sections.forEach((section, secIndex) => {
                section.style.display = index === secIndex ? "block" : "none";
            });

            form.style.display = index >= sections.length ? "block" : "none";
        });
    });

    // Default visibility setup
    sections.forEach((section, index) => {
        section.style.display = index === 0 ? "block" : "none";
    });
    form.style.display = "none";

    // Add Address button functionality
    addAddressBtn.addEventListener("click", () => {
        const newAddress = prompt("Enter a new address:");
        if (newAddress) {
            const li = document.createElement("li");
            li.textContent = newAddress;
            addressList.appendChild(li);
        }
    });

    // Form submission handler
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        alert("Profile updated successfully!");
    });
});


