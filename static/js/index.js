// JavaScript code for the main page index.html


// Functions when you click the search icon
function clickSearchButton() {
    element = document.getElementById("search-icon");
    element.setAttribute('src', 'static/assets/search_white.png');
}

function unclickSearchButton() {
    element = document.getElementById("search-icon");
    element.setAttribute('src', 'static/assets/search_black.png');
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

// Array of random search queries
const searchQueries = [
    "speech recognition using DeepSpeech",
    "data analysis with Pandas in Jupyter Notebook",
    "Find repositories related to chatbot development with Rasa",
    "data visualization with D3.js",
    "Find repo of a game build with pygame",
    "web application development using the Django framework",
    "cloud computing using AWS services",
    "cybersecurity repos in Python or Java",
    "all the repos by microsoft",
    "cryptography with the apache license",
    "find repos related to artificial intelligence with the apache license",
    "clones of the super mario game",
    "microservices architecture with Spring Boot",
    "virtual reality development with Unity3D distributed with apache",
    "computer graphics using OpenGL",
    "software testing with Selenium",
    "calculator app with tkinter",
    "Search for repositories about distributed systems with Apache Kafka",
    "Find repositories related to web development with React",
    "data science in Python",
    "machine learning and image recognition in python",
    "secure coding in Java and C++",
    "web application security with OWASP"
];
