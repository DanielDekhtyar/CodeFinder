// When the user clicks on the logo, go back to the home page
const logo = document.getElementById("logo")
logo.addEventListener("click", () => {
    window.location.href = "/";
})