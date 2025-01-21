// JavaScript to load positions based on division
document.getElementById('division').addEventListener('change', function () {
    const divisionId = this.value;
    const positionDropdown = document.getElementById('position');

    // Clear previous position options
    positionDropdown.innerHTML = '<option value="">Select Position</option>';

    if (divisionId) {
        // Send request to server to get positions
        fetch(`/positions/${divisionId}`)
            .then(response => response.json())
            .then(data => {
                // Add position options received from the server
                data.positions.forEach(position => {
                    const option = document.createElement('option');
                    option.value = position.id;
                    option.textContent = position.name;
                    positionDropdown.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching positions:', error));
    }
});

// Show popup if 'success' parameter exists in URL
window.onload = function () {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('success')) {
        const popup = document.getElementById('success-popup');
        const overlay = document.getElementById('overlay');

        popup.style.display = 'block';
        overlay.style.display = 'block';

        // Close popup on button click
        document.getElementById('close-popup').addEventListener('click', function () {
            popup.style.display = 'none';
            overlay.style.display = 'none';
        });
    }
};

// Toggle password visibility
function setupPasswordToggle(inputId, toggleButtonId) {
    const inputField = document.getElementById(inputId);
    const toggleButton = document.getElementById(toggleButtonId);

    toggleButton.addEventListener('click', function () {
        const isPasswordVisible = inputField.type === 'text';
        inputField.type = isPasswordVisible ? 'password' : 'text';
        toggleButton.textContent = isPasswordVisible ? 'Show' : 'Hide';
    });
}

// Setup toggles for password and confirm password fields
setupPasswordToggle('password', 'togglePassword');
setupPasswordToggle('confirmPassword', 'toggleConfirmPassword');

// Validate password match on form submission
document.getElementById('registerForm').addEventListener('submit', function (event) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const errorMsg = document.getElementById('errorMsg');

    if (password !== confirmPassword) {
        event.preventDefault(); // Prevent form submission
        errorMsg.textContent = 'Passwords do not match. Please try again.';
    } else {
        errorMsg.textContent = ''; // Clear error message
    }
});