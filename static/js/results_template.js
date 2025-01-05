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

// Make the header appear and disappear when you scroll up or down responsively
document.addEventListener("DOMContentLoaded", function() {
    var header = document.getElementById("header");
    var lastScrollY = window.scrollY;

    window.addEventListener("scroll", function() {
        if (window.scrollY > lastScrollY) {
            // Scrolling down
            header.style.top = "-4.5rem"; // Hide the header
        } else {
            // Scrolling up
            header.style.top = "0"; // Show the header
        }
        lastScrollY = window.scrollY;
    });
});

// Check if the search for is not empty. If it is empty, make the border red. Else send the request
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

// Start the loading screen effect
function loading_screen() {
    // Scroll to the top of the page and hide to prevent scrolling behind the loading screen
    // Scroll to top
    window.scrollTo(0, 0);

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

    // Hide all the search results to make the page un-scrollable by fitting it in to the viewport
    document.getElementById("search-results").style.display = "none";
}

window.addEventListener('DOMContentLoaded', function() {
    var contentHeight = document.body.clientHeight;
    var viewportHeight = window.innerHeight;
    var footer = document.getElementById('footer');

    if (contentHeight < viewportHeight) {
        footer.style.position = 'absolute';
    }
});

// Functions when you hover over the search icon
function hoverFilterButton() {
    element = document.getElementById("filter-icon");
    element.setAttribute('src', 'static/assets/filter_hover.png');
}

// Functions when you hover over the search icon
function unhoverFilterButton() {
    element = document.getElementById("filter-icon");
    element.setAttribute('src', 'static/assets/filter.png');
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
