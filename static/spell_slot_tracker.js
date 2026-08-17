document.addEventListener("DOMContentLoaded", () => {
    // Load saved options
    if (localStorage.getItem("class")) {
        document.getElementById("class").value = localStorage.getItem("class");
    }
    if (localStorage.getItem("level")) {
        document.getElementById("level").value = localStorage.getItem("level");
    }

    // Save options on form submit
    document.querySelector("form").addEventListener("submit", () => {
        localStorage.setItem("class", document.getElementById("class").value);
        localStorage.setItem("level", document.getElementById("level").value);
    });
});