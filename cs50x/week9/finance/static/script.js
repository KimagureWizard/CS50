document.addEventListener("DOMContentLoaded", function() {
    let registerForm = document.querySelector("#register_form");
    let password = document.querySelector("#password");
    let passwordCheck = document.querySelector("#password_check");
    const re = /\b[A-Z]\w{7,}\b/;

    registerForm.addEventListener("submit", function(event) {
        if (!re.test(password.value)) {
            alert("Password must contain at least 8 characters, and start with one uppercase letter");
            password.value = "";
            passwordCheck.value = "";
            event.preventDefault();
        }
        else if (password.value !== passwordCheck.value) {
            alert("Passwords do not match");
            password.value = "";
            passwordCheck.value = "";
            event.preventDefault();
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    let passwordForm = document.querySelector("#password_form");
    let newPassword = document.querySelector("#new_password");
    let newPasswordCheck = document.querySelector("#new_password_check");
    const re = /\b[A-Z]\w{7,}\b/;

    passwordForm.addEventListener("submit", function(event) {
        if (!re.test(newPassword.value)) {
            alert("Password must contain at least 8 characters, and start with one uppercase letter.");
            newPassword.value = "";
            newPasswordCheck.value = "";
            event.preventDefault();
        }
        else if (newPassword.value !== newPasswordCheck.value) {
            alert("Passwords do not match");
            newPassword.value = "";
            newPasswordCheck.value = "";
            event.preventDefault();
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    let selectMenu = document.querySelector("#select_menu");
    let defaultProfilePic = document.querySelector("#default_profile_pic");

    selectMenu.addEventListener("change", function(event) {
        if (selectMenu.selectedIndex === 1) {
            defaultProfilePic.src = "/static/cat.jpg";
        } else if (selectMenu.selectedIndex === 2) {
            defaultProfilePic.src = "/static/hotdog.jpg";
        } else {
            defaultProfilePic.src = "/static/potato.png";
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    let selectMenu = document.querySelector("#select_menu");
    let profilePicNav = document.querySelector("#profile_pic_nav");
    let profilePic = document.querySelector("#profile_pic");

    selectMenu.addEventListener("change", function(event) {
        let selectedOption = selectMenu.value;
        let imagePath = "";

        if (selectedOption === "cat") {
            imagePath = "/static/cat.jpg";
        } else if (selectedOption === "hotdog") {
            imagePath = "/static/hotdog.jpg";
        } else {
            imagePath = "/static/potato.png";
        }

        profilePicNav.src = imagePath;
        profilePic.src = imagePath;
        localStorage.setItem("profile_pic", imagePath);
    });
});

document.addEventListener("DOMContentLoaded", function() {
    let topupForm = document.querySelector("#topup_form");
    let topup = document.querySelector("#topup");

    topupForm.addEventListener("submit", function(event) {
        if (topup.value == "") {
            alert("Please type in a number.");
            event.preventDefault();
        }
    });
});
