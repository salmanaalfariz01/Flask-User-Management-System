// Show or hide password functionality
document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    const showPasswordToggle = document.getElementById('showPassword');

    showPasswordToggle.addEventListener('change', () => {
        if (showPasswordToggle.checked) {
            passwordInput.type = 'text';
        } else {
            passwordInput.type = 'password';
        }
    });
});
