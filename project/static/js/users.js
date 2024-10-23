document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const username = document.querySelector('#username');
        const email = document.querySelector('#email');
        const password = document.querySelector('#password');
        const role = document.querySelector('#role');

        // Check for empty fields
        if (username.value.trim() === '' || email.value.trim() === '' || password.value.trim() === '' || role.value.trim() === '') {
            alert('All fields are required to create a new user.');
            event.preventDefault();
            return; // Stop further execution
        }

        // Check username and role length
        if (username.value.length > 20 || role.value.length > 20) {
            alert('Username and role must be under 20 characters.');
            event.preventDefault();
            return; // Stop further execution
        }

        // Check email length
        if (email.value.length > 125) {
            alert('Email must be under 125 characters.');
            event.preventDefault();
            return; // Stop further execution
        }

        // Unique username check
        const existingUsernames = Array.from(document.querySelectorAll('td:nth-child(1)')).map(td => td.textContent.trim());
        if (existingUsernames.includes(username.value.trim())) {
            alert('Username already exists. Please choose a different username.');
            event.preventDefault();
            return; // Stop further execution
        }
    });
});