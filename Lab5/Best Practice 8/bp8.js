const btn = document.getElementById("btn");
function handleClick() {
    alert("Clicked!");
}
btn.addEventListener("click", handleClick);
// When no longer needed:
// btn.removeEventListener("click", handleClick);