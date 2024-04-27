// When the page loads, run the functions
window.onload = function() {
    truncateHomepage();
    truncateDescription();
}

// If the homepage link is too long, truncate it
function truncateHomepage() {
    var homepages = document.getElementsByClassName("homepage");
    for (var i = 0; i < homepages.length; i++) {
        var homepage = homepages[i];
        var link = homepage.querySelector("a"); // Find the anchor element inside the paragraph
        if (link) {
            var text = link.textContent; // Get the text content of the anchor element
            if (text.length > 50) {
                // Truncate the text content and set it back
                link.textContent = text.substring(0, 50) + "...";
            }
        }
    }
}

// If the description is too long, truncate it
function truncateDescription() {
    var descriptions = document.getElementsByClassName("description");
    for (var i = 0; i < descriptions.length; i++) {
        var description = descriptions[i];
        var description_count = descriptionLength(description.textContent);
        if (description_count.wordCount >= 50) {
            // Truncate the text content and set it back
            description.innerHTML = description.textContent.substring(0, description_count.characterCount) + ' <span class="see-more"> [See the rest of the description on GitHub]</span>';
        }
    }
}

function descriptionLength(inputString) {
    // Split the input string into words
    var words = inputString.split(/\s+/);
    var characterCount = 0;
    var wordCount = 0;

    // Iterate through the words
    for (var i = 0; i < words.length; i++) {
        // Add the length of each word plus 1 (for the space) to the character count
        characterCount += words[i].length + 1;
        wordCount++;

        // Check if we have reached the 50th word
        if (wordCount >= 50) {
            break;
        }
    }

    // Subtract 1 to remove the last added space
    characterCount--;

    return { characterCount: characterCount, wordCount: wordCount };
}
