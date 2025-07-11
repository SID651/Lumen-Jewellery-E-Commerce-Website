document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.new-product-cart-btn');

    buttons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const productBox = button.closest('.new-product-box');
            const productId = productBox.getAttribute('data-product-id');
            
            // Send an AJAX request to add the product to the cart
            fetch('/add-to-cart', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ productId })
            })
            .then(response => {
                if (response.ok) {
                    // Redirect to cart page
                    window.location.href = '/cart';
                } else {
                    console.error('Failed to add product to cart');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});
