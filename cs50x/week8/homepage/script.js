document.addEventListener("DOMContentLoaded", function() {
    let contents = document.querySelectorAll(".content");
    let thumbnails = document.querySelectorAll(".thumbnail-img");

    contents.forEach(function(content) {
        content.addEventListener("mouseover", function(event) {
            content.style.backgroundColor = "#0d0d0d";
            content.style.color = "#4dd2ff";
            content.style.borderColor = "#4dd2ff";
        });
        content.addEventListener("mouseout", function(event) {
            content.style.backgroundColor = "";
            content.style.color = "";
            content.style.borderColor = ""
        });
    });

    thumbnails.forEach(function(thumbnail) {
        thumbnail.addEventListener("mouseover", function(event) {
          thumbnail.style.transform = "scale(1.2)";
        });

        thumbnail.addEventListener("mouseout", function(event) {
          thumbnail.style.transform = "";
        });
      });
});