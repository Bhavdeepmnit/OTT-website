document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    // Send a request to the server for authentication
    fetch("/authenticate", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"  // Use URL-encoded form data
        },
        body: new URLSearchParams({
            'username': username,
            'password': password
        })
    })
    .then(response => {
        if (response.ok) {
            // Redirect to dashboard or another page upon successful login
            window.location.href = "/index.html";
        } else {
            // Display error message for invalid credentials
            alert("Invalid username or password. Please try again.");
        }
    })
    .catch(error => console.error("Error:", error));
});
