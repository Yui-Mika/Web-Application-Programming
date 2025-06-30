function sanitize(input) {
    // Remove any script tags
    return input.replace(/[<>"']/g, "");
}
function showSanitized() {
    const raw = document.getElementById('userInput').value;
    document.getElementById('out').textContent = "Safe: " + sanitize(raw);
}