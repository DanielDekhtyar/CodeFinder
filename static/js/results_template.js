// When the user clicks on the logo, go back to the home page
const logo = document.getElementById("logo")
logo.addEventListener("click", () => {
    window.location.href = "/";
})

// Functions when you hover over the search icon
function hoverSearchButton() {
    element = document.getElementById("search-icon");
    element.setAttribute('src', 'static/assets/search_white.png');
}

// Functions when you hover over the search icon
function unhoverSearchButton() {
    element = document.getElementById("search-icon");
    element.setAttribute('src', 'static/assets/search_black.png');
}

// Functions when you hover over the forward button
function hoverForwardButton() {
    element = document.getElementById("forward-button");
    element.setAttribute('src', 'static/assets/forward black.png');
}

function unhoverForwardButton() {
    element = document.getElementById("forward-button");
    element.setAttribute('src', 'static/assets/forward.png');
}

// Functions when you hover over the back button
function hoverBackButton() {
    element = document.getElementById("back-button");
    element.setAttribute('src', 'static/assets/back black.png');
}

// Functions when you hover over the back button
function unhoverBackButton() {
    element = document.getElementById("back-button");
    element.setAttribute('src', 'static/assets/back.png');
}

// Get the input element
var searchBar = document.getElementsByClassName("form-control")[0];

// Event listener for when the input box gains focus
searchBar.addEventListener("focus", function() {
    // Reset the placeholder text when the input box gains focus
    this.placeholder = "What are you looking for?";
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
        console.log("placeholder changed");
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

function loading_screen() {
    // Hide the footer
    document.getElementById('footer').style.display = 'none';
    
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

function page_turn() {
    // Scroll to top
    window.scrollTo(0, 0);

    // Hide all the search results to make the page smaller and un-scrollable
    document.getElementById("search-results").style.display = "none";

    // Show the loading screen
    loading_screen();
}
