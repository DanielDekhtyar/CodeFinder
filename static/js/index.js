// JavaScript code for the main page index.html

// Get the input element
var searchBar = document.getElementsByClassName("form-control")[0];

// Defining what a small screen is
const isSmallScreen = window.matchMedia("(max-width: 600px)").matches;

// Event listener for when the input box gains focus
searchBar.addEventListener("focus", function() {
    // Reset the placeholder text when the input box gains focus
    // Check if the screen width is less than or equal to 600px (small screens)
    if (isSmallScreen) {
        this.placeholder = "Find any repository on GitHub!";
    } else {
        this.placeholder = "Find any repository on GitHub! Just type and hit enter...";
    }
    
    // Remove the "empty-input" class from the input element, if it was there
    var searchInput = document.getElementById("search-bar");
    searchInput.classList.remove("empty-input");
});

// Event listener for when the input box loses focus
searchBar.addEventListener("blur", function() {
    // Check if the input box is empty
    if (!this.value.trim()) {
        // Change the placeholder text
        this.placeholder = "Type [/] to search";
    }
});

// Event listener for when the '/' key is pressed
document.addEventListener("keydown", function(event) {
    // Check if the '/' key is pressed
    if (event.key === '/') {
        // Prevent the default behavior of the '/' key press event
        event.preventDefault();
        
        // Set focus to the input element
        searchBar.focus();
        
        // Set the cursor at the end of the current text
        var currentTextLength = searchBar.value.length;
        searchBar.setSelectionRange(currentTextLength, currentTextLength);
    }
});

function setSearchPlaceholderOnLoading() {
    const searchBar = document.getElementById("search-bar");

    if (!searchBar) {
        console.error("Search bar not found");
        return;
    }

    // Check screen size
    if (isSmallScreen) {
        searchBar.placeholder = "Find any repository on GitHub!";
    } else {
        searchBar.placeholder = "Find any repository on GitHub! Just type and hit enter...";
    }
}

// Run on page load
setSearchPlaceholderOnLoading();

// Listen for screen resize
window.addEventListener("resize", setSearchPlaceholderOnLoading);


// Check if the input form is not empty. If it is empty, make the border red.
function validateForm() {
    var searchInput = document.getElementById("search-bar");
    var inputValue = searchInput.value.trim();
    if (inputValue === "") {
        // Search box borders become red, indicating an error
        searchInput.classList.add("empty-input");
        return false; // Prevent the form from submitting
    } else {
        searchInput.classList.remove("empty-input");
        loading_screen();
        return true; // Allow the form to submit
    }
}

// Functions when you click the search icon
function clickSearchButton() {
    element = document.getElementById("search-icon");
    element.setAttribute('src', 'static/assets/search_hover.png');
}

function unclickSearchButton() {
    element = document.getElementById("search-icon");
    element.setAttribute('src', 'static/assets/search_black.png');
}

// Functions when you hover over the filter icon
function hoverFilterButton() {
    element = document.getElementById("filter-icon");
    element.setAttribute('src', 'static/assets/filter_hover.png');
}

function unhoverFilterButton() {
    element = document.getElementById("filter-icon");
    element.setAttribute('src', 'static/assets/filter.png');
}

// Functions when you hover over the random search icon
function hoverRandomSearchButton() {
    element = document.getElementById("dice-icon");
    element.setAttribute('src', 'static/assets/dice_hover.png');
}

function unhoverRandomSearchButton() {
    element = document.getElementById("dice-icon");
    element.setAttribute('src', 'static/assets/dice.png');
}

// Function to show the loading screen animation
function loading_screen() {
    // Hide the footer
    document.getElementById('footer').style.display = 'none';

    // Hide hostage timer
    document.getElementById('bthn').style.display = 'none';
    
    // Make all the elements of the loading screen visible
    // Change the CSS for load-wrapper (div)
    document.getElementsByClassName('loader-wrapper')[0].style.display = 'flex';
    document.getElementById('loader-wrapper').classList.add('loader-wrapper-hover');

    // Change the CSS for loader
    document.getElementsByClassName('loader')[0].style.animation = 'loader 2s infinite ease';
    document.getElementsByClassName('loader')[0].style.display = 'inline-block';

    // Change the CSS for loader-inner
    document.getElementsByClassName('loader-inner')[0].style.animation = 'loader-inner 2s infinite ease-in';
    document.getElementsByClassName('loader-inner')[0].style.display = 'inline-block';
}

// Function to get a random search query from the array
function randomSearch() {
    // Get a random search query
    const randomIndex = Math.floor(Math.random() * searchQueries.length);
    var random_string = searchQueries[randomIndex];
    
    // Put the search query in the input box
    var inputBox = document.getElementById("search-bar");
    inputBox.value = random_string;

    // Call the function to validate the form
    validateForm();

    // Submit the form
    document.getElementById("search-form").submit();
}


// Filter Modal opening and closing functions
const openFilterModalButton = document.getElementById("filter-button");
const closeFilterModalButton = document.getElementsByClassName("close-modal-button")[0];

// Show the filter modal on the screen
function openFilterModal() {
    const modalOverlay = document.getElementById("modal-overlay");
    const modal = document.getElementById("filter-modal");

    modalOverlay.classList.add("active");
    modal.classList.add("active");
}

function closeFilterModal() {
    const modalOverlay = document.getElementById("modal-overlay");
    const modal = document.getElementById("filter-modal");

    modalOverlay.classList.remove("active");
    modal.classList.remove("active");
}

document.addEventListener('DOMContentLoaded', function() {
    const dropdownButton = document.getElementById('dropdownMenuButton');
    const dropdownMenu = document.querySelector('.menu');
    const searchInput = document.getElementById('search-input');
    const optionList = document.getElementById('option-list');
    const items = optionList.querySelectorAll('.dropdown-item');
    const selectedLanguagesInput = document.getElementById('selected-languages');
    const selectedAuthorInput = document.getElementById('selected-author');
    const selectedLastUpdateInput = document.getElementById('selected-last-update');
    const selectedStarsInput = document.getElementById('selected-stars');
    const lastPushedDateInput = document.getElementById('last-pushed-date');
    const authorInput = document.getElementById('author-input');
    const starsInput = document.getElementById('stars-input');

    let selectedItems = [];

    dropdownButton.addEventListener('click', function() {
        dropdownMenu.classList.toggle('menu-open');
        dropdownButton.classList.toggle('select-clicked');
        document.querySelector('.caret').classList.toggle('caret-rotate');
    });

    document.addEventListener('click', function(event) {
        if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove('menu-open');
            dropdownButton.classList.remove('select-clicked');
            document.querySelector('.caret').classList.remove('caret-rotate');
        }
    });

    searchInput.addEventListener('input', function() {
        const filter = this.value.toLowerCase();
        items.forEach(function(item) {
            const text = item.textContent || item.innerText;
            item.style.display = text.toLowerCase().indexOf(filter) > -1 ? 'flex' : 'none';
        });
    });

    items.forEach(function(item) {
        item.addEventListener('click', function() {
            const value = item.getAttribute('data-value');
            if (selectedItems.includes(value)) {
                selectedItems = selectedItems.filter(i => i !== value);
                item.classList.remove('selected');
            } else {
                selectedItems.push(value);
                item.classList.add('selected');
            }
            updateDropdownText();
            updateSelectedLanguagesInput();
            console.log('Selected items:', selectedItems);
        });
    });

    function updateDropdownText() {
        if (selectedItems.length > 0) {
            const selectedNames = Array.from(items).filter(item => selectedItems.includes(item.getAttribute('data-value')))
                .map(item => item.textContent || item.innerText);
            dropdownButton.querySelector('span').textContent = selectedNames.join(', ');
        } else {
            dropdownButton.querySelector('span').textContent = 'Select Language';
        }
    }

    function updateSelectedLanguagesInput() {
        selectedLanguagesInput.value = selectedItems.join(',');
    }

    window.applyFilters = function() {
        selectedAuthorInput.value = authorInput.value;
        selectedLastUpdateInput.value = lastPushedDateInput.value;
        selectedStarsInput.value = starsInput.value;
        closeFilterModal();
    };
});

// Countdown Timer Logic
const countdownElement = document.getElementById("countdown-timer");
// Set the date we're counting down to (May 1st, 2025)
const targetDate = new Date("May 1, 2025 00:00:00").getTime();

function updateCountdown() {
    // Get today's date and time
    const now = new Date().getTime();

    // Find the distance between now and the count down date
    const distance = targetDate - now;

    // If the count down is finished, write some text
    if (distance < 0) {
        if (countdownElement) {
            countdownElement.innerHTML = "The deadline has passed!";
        }
        clearInterval(countdownInterval); // Stop the interval
        return;
    }

    // Time calculations for days, hours, minutes and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Build the display string
    let countdownText = "";
    if (days > 0) countdownText += days + "d ";
    if (hours > 0 || days > 0) countdownText += hours + "h ";
    if (minutes > 0 || hours > 0 || days > 0) countdownText += minutes + "m ";
    countdownText += seconds + "s";

    // Display the result in the element with id="countdown-timer"
    if (countdownElement) {
        countdownElement.innerHTML = countdownText.trim();
    }
}

// Update the count down every 1 second only if the element exists
let countdownInterval;
if (countdownElement) {
    countdownInterval = setInterval(updateCountdown, 1000);
    // Initial call to display the countdown immediately
    updateCountdown();
}

// Array of random search queries
const searchQueries = [
    "speech recognition using DeepSpeech",
    "data analysis with Pandas in Jupyter Notebook",
    "Find repositories related to chatbot development with Rasa",
    "data visualization with D3.js",
    "snake game using pygame",
    "web application using the Flask framework",
    "Capture the flag (CTF)",
    "all the repos by microsoft",
    "IoT using Arduino",
    "cryptography with the apache license",
    "clones of the super mario game",
    "microservices architecture with Spring Boot",
    "virtual reality development with Unity3D",
    "QA tools",
    "calculator app with tkinter",
    "Find repositories related to web development with React",
    "data science using Pandas library",
    "facial recognition in python",
    "Android development with Kotlin",
];

// Functions when you hover over the Product Hunt badge
document.addEventListener("DOMContentLoaded", function() {
    var productHuntImg = document.getElementById("product-hunt-img");

    productHuntImg.addEventListener("mouseover", function() {
        productHuntImg.src = "https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=462813&theme=light";
    });

    productHuntImg.addEventListener("mouseout", function() {
        productHuntImg.src = "https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=462813&theme=neutral";
    });
});
