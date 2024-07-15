let screen = document.getElementById("screen")
buttons = document.querySelectorAll("button")
let screenvalue = " ";


for (item of buttons) {
    item.addEventListener("click", (e) => {
        buttonText = e.target.innerText
        if (buttonText == "X") {
            buttonText = "*"
            screenvalue += buttonText
            screen.value = screenvalue
        }
        else if (buttonText == "C") {
            screenvalue = " ";
            screen.value = screenvalue
        }
        else if (buttonText == "=") {
            screen.value = eval(screenvalue)
        }
        else {
            screenvalue += buttonText
            screen.value = screenvalue
        }
    })
}
