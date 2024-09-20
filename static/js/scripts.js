window.onload = function () {
    const form = document.querySelector('form');
    const messageBox = document.getElementById('message-box');
    
    if (messageBox) {
        setTimeout(() => {
            messageBox.style.display = 'none';
        }, 1500);
    }

    form.addEventListener('submit', function (event) {
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;
        const errors = [];

        if (password !== confirmPassword) {
            errors.push('Passwords do not match!');
        }

        if (errors.length > 0) {
            event.preventDefault();
            showErrors(errors);
        }
    });

    function showErrors(errors) {
        if (messageBox) {
            messageBox.innerHTML = '';
            messageBox.style.display = 'block';

            errors.forEach(error => {
                const errorDiv = document.createElement('div');
                errorDiv.classList.add('message', 'error');
                errorDiv.textContent = error;
                messageBox.appendChild(errorDiv);
            });

            // Check for server-side errors as well
            const serverErrors = document.querySelectorAll('.form-group .error');
            serverErrors.forEach(errorElement => {
                const errorDiv = document.createElement('div');
                errorDiv.classList.add('message', 'error');
                errorDiv.innerHTML = errorElement.innerHTML;
                messageBox.appendChild(errorDiv);
            });
        } else {
            console.warn('Message box element not found');
        }
    }
};
