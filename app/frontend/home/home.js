document.addEventListener("DOMContentLoaded", function () {
    // Get session expiry time from server
    const sessionExpiry = "{{ session.get('session_expiry') }}";

    if (sessionExpiry) {
        const expiryDate = new Date(sessionExpiry);
        const now = new Date();

        const timeRemaining = expiryDate - now;

        if (timeRemaining > 0) {
            // Logout and redirect after session expires
            setTimeout(() => {
                alert("Your session has expired. You will be logged out now.");
                window.location.href = "{{ url_for('logout.show') }}"; // Logout and redirect
            }, timeRemaining);
        }
    }
});
