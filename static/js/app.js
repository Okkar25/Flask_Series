console.log("Hello World");

// window.onload = () => {
//     setTimeout(() => {
//         alert("Please do not forget tot learn Django")
//     }, 2000)
// }

const specialText = document.querySelector('.special');

isTrue = true

specialText.addEventListener("click", (event) => {

    isTrue = !isTrue
    // console.log(isTrue);

    if (isTrue){
        event.target.innerText = "This is CSS Stylesheet"
    } else {
        event.target.innerText = "This is JavaScript Scripting"
    }

    event.target.classList.toggle("special")
})