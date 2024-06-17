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