document.addEventListener('DOMContentLoaded', () => {
    const quantityButtons = document.querySelectorAll('.quantity-button');
    
    quantityButtons.forEach(button => {
        button.addEventListener('click', () => {
            const action = button.getAttribute('data-action');
            const itemId = button.getAttribute('data-id');
            const quantityInput = document.querySelector(`input[name="${itemId}"]`);
            let currentValue = parseInt(quantityInput.value);
            
            if (action === 'increase') {
                quantityInput.value = currentValue + 1;
            } else if (action === 'decrease') {
                if (currentValue > 1) {
                    quantityInput.value = currentValue - 1;
                }
            }
        });
    });
});
