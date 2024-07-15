var pass = document.getElementById("password");
var msg = document.getElementById("message");
var str = document.getElementById("strength");
var eyeIcon = document.getElementById("eyeicon");


function updatePasswordStrength() {
    if(pass.value.length > 0){
        msg.style.display = "block";
    } else {
        msg.style.display = "none";
    }

    if(pass.value.length < 4){
        str.innerHTML = "weak";
        pass.style.borderColor = "red";
        msg.style.color = "red";
    } else if (pass.value.length >= 4 && pass.value.length < 8) {
        str.innerHTML = "medium";
        pass.style.borderColor = "yellow";
        msg.style.color = "yellow";
    } else if (pass.value.length >= 8) {
        str.innerHTML = "strong";
        pass.style.borderColor = "green";
        msg.style.color = "green";
    }
}


function togglePasswordVisibility() {
    if (pass.type === "password") {
        pass.type = "text";
        eyeIcon.src = "eye-open.png";
    } else {
        pass.type = "password";
        eyeIcon.src = "eye-close.png";
    }
}


pass.addEventListener("input", updatePasswordStrength);
eyeIcon.addEventListener("click", togglePasswordVisibility);
