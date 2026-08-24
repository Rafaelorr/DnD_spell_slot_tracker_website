document.addEventListener("DOMContentLoaded", () => {
    const fields = ["class", "level", "level_1", "level_2", "level_3", "level_4", "level_5", "level_6", "level_7", "level_8", "level_9"];

    // Load saved options from localStorage
    fields.forEach(field => {
        const element = document.getElementById(field);
        if (element && localStorage.getItem(field)) {
            element.value = localStorage.getItem(field);
        }
    });

    // Save options to localStorage on change
    fields.forEach(field => {
        const element = document.getElementById(field);
        if (element) {
            element.addEventListener("change", () => {
                localStorage.setItem(field, element.value);
            });
        }
    });

    // Reference class and level elements
    const classElem = document.getElementById("class");
    const levelElem = document.getElementById("level");

    // Fetch and update spell slots when class or level changes
    if (classElem && levelElem) {
        classElem.addEventListener("change", fetchAndUpdateSpellSlots);
        levelElem.addEventListener("change", fetchAndUpdateSpellSlots);
    }

    // Load saved class and level and fetch spell slots initially
    if (localStorage.getItem("class")) classElem.value = localStorage.getItem("class");
    if (localStorage.getItem("level")) levelElem.value = localStorage.getItem("level");
    fetchAndUpdateSpellSlots();

    // Save spell slot values and selections on form submit
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", () => {
            for (let i = 1; i <= 9; i++) {
                const input = document.getElementById(`level_${i}`);
                if (input) {
                    localStorage.setItem(`level_${i}`, input.value);
                }
            }
            // Save current class and level selections
            if (classElem) localStorage.setItem("class", classElem.value);
            if (levelElem) localStorage.setItem("level", levelElem.value);
        });
    }
});

// Function to fetch spell slots data based on class and level
function fetchAndUpdateSpellSlots() {
    const classSelect = document.getElementById("class");
    const levelSelect = document.getElementById("level");
    if (!classSelect || !levelSelect) return;

    const selectedClass = classSelect.value;
    const selectedLevel = levelSelect.value;

    fetch(`/get_spell_slots?class=${encodeURIComponent(selectedClass)}&level=${encodeURIComponent(selectedLevel)}`)
        .then(response => response.json())
        .then(data => {
            for (let i = 1; i <= 9; i++) {
                const input = document.getElementById(`level_${i}`);
                if (input) {
                    input.value = data[`level_${i}`] || 0;
                    localStorage.setItem(`level_${i}`, input.value);
                }
            }
            // Save class and level to local storage
            localStorage.setItem("class", selectedClass);
            localStorage.setItem("level", selectedLevel);
        })
        .catch(error => {
            console.error("Error fetching spell slots:", error);
        });
}