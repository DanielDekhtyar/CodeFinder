document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    fetch('https://formspree.io/f/mrgnnqde', {
        method: 'POST',
        headers: {
            'Accept': 'application/json'
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.ok) {
            showPopup('Thank you for getting in touch! We will get back to you soon.');
            this.reset(); // Reset the form after successful submission
        } else {
            showPopup('There was an error sending your message. Please try again later.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showPopup('There was an error sending your message. Please try again later.');
    });
});

function showPopup(message) {
    const popup = document.getElementById('popup');
    popup.textContent = message;
    popup.style.display = 'block';
    setTimeout(function() {
        popup.style.display = 'none';
    }, 5000); // Hide popup after 5 seconds
}
