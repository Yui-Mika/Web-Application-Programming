let cart = [];
function addToCart(name, price) {
    cart.push({ name, price});
    renderCart();
}

function removeItem(index) {
    cart.splice(index, 1);
    renderCart();
}

function renderCart() {
    const cartUl = document.getElementById('cart');
    cartUl.innerHTML = "";
    cart.forEach((item, i) => {
        cartUl.innerHTML += `<li>${item.name} - ($${item.price}) <button onclick="removeItem(${i})">Remove</button></li>`;
    });
    document.getElementById('total').textContent = "Total: $" + cart.reduce((sum, item) => sum + item.price, 0);
}