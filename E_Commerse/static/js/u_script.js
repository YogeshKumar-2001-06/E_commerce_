document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".tab");
    const sections = document.querySelectorAll(".details-section");
    const form = document.querySelector(".form");

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


    // Form submission handler
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        alert("Profile updated successfully!");
    });
});


