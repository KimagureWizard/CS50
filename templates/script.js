document.addEventListener("DOMContentLoaded", function() {
    let thumbnails = document.querySelectorAll(".thumbnail-img");

    thumbnails.forEach(function(thumbnail) {
        thumbnail.addEventListener("mouseover", function(event) {
          thumbnail.style.transform = "scale(1.2)";
        });

        thumbnail.addEventListener("mouseout", function(event) {
          thumbnail.style.transform = "";
        });
    });
});