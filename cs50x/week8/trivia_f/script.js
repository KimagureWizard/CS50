document.addEventListener("DOMContentLoaded", function() {
    let choices = document.querySelectorAll(".choice");
    let feedback1 = document.querySelector("#feedback1");
    let isAnswered = false;

    choices.forEach(function(choice) {
        choice.addEventListener("mouseover", function(event) {
            if (!isAnswered) {
            choice.style.backgroundColor = "white";
            }
        });
        choice.addEventListener("mouseout", function(event) {
            if (!isAnswered) {
            choice.style.backgroundColor = "#d9edff";
            }
        });
        choice.addEventListener("click", function(event) {
            if(choice.textContent == "Legend Of Zelda: BoW") {
                feedback1.style.marginLeft = "270px";
                choice.style.backgroundColor = "red";
                feedback1.innerHTML = "Incorrect";
            }
            else if(choice.textContent == "God Of War") {
                feedback1.style.marginLeft = "130px";
                choice.style.backgroundColor = "red";
                feedback1.innerHTML = "Incorrect";
            }
            else if(choice.textContent == "Elden Ring") {
                feedback1.style.marginLeft = "20px";
                choice.style.backgroundColor = "red";
                feedback1.innerHTML = "Incorrect";
            }
            else {
                feedback1.innerHTML = "Correct!";
                isAnswered = true;
                choice.style.backgroundColor = "green";
                feedback1.style.marginLeft = "450px";
            }
        });
    });

    let answer = document.querySelector("#answer");
    let feedback2 = document.querySelector("#feedback2");
    let check = document.querySelector("#check");

    check.addEventListener("mouseover", function(event) {
        check.style.backgroundColor = "white";
    });
    check.addEventListener("mouseout", function(event) {
        check.style.backgroundColor = "#d9edff";
    });
    check.addEventListener("click", function(event) {
        if(answer.value != "8") {
            answer.style.backgroundColor = "red";
            feedback2.innerHTML = "Incorrect";
        }
        else {
            answer.style.backgroundColor = "green";
            feedback2.innerHTML = "Correct!";
        }
    });
});