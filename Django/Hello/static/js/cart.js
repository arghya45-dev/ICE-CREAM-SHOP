document.addEventListener("DOMContentLoaded", function () {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    function updateCartDisplay() {
        let cartItems = document.getElementById("cart-items");
        let cartTotal = document.getElementById("cart-total");
        cartItems.innerHTML = "";
        let total = 0;

        cart.forEach((item, index) => {
            let li = document.createElement("li");
            li.className = "list-group-item d-flex justify-content-between align-items-center bg-secondary text-light";
            li.innerHTML = `
                ${item.name} - ₹${item.price} x 
                <input type="number" min="1" value="${item.quantity}" class="cart-quantity" data-index="${index}" style="width: 50px;">
                <button class="btn btn-danger btn-sm remove-item" data-index="${index}">Remove</button>
            `;
            cartItems.appendChild(li);
            total += item.price * item.quantity;
        });

        cartTotal.innerText = total;
        localStorage.setItem("cart", JSON.stringify(cart));
    }

    document.getElementById("cart-items").addEventListener("change", function (e) {
        if (e.target.classList.contains("cart-quantity")) {
            let index = e.target.getAttribute("data-index");
            cart[index].quantity = parseInt(e.target.value);
            updateCartDisplay();
        }
    });

    document.getElementById("cart-items").addEventListener("click", function (e) {
        if (e.target.classList.contains("remove-item")) {
            let index = e.target.getAttribute("data-index");
            cart.splice(index, 1);
            updateCartDisplay();
        }
    });

    document.getElementById("clear-cart").addEventListener("click", function () {
        cart = [];
        updateCartDisplay();
    });

    updateCartDisplay();
});
