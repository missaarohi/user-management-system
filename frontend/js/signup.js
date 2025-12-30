async function signup() {
    const full_name = document.getElementById("full_name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;

body: JSON.stringify({
    full_name,
    email,
    password,
    role
})
    const error = document.getElementById("error");
    const success = document.getElementById("success");

    error.innerText = "";
    success.innerText = "";

    if (!full_name || !email || !password) {
        error.innerText = "All fields are required";
        return;
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                full_name,
                email,
                password
            })
        });

        const data = await res.json();

        if (!res.ok) {
            error.innerText = data.error || "Signup failed";
            return;
        }

        success.innerText = "Signup successful! Redirecting to login...";

        setTimeout(() => {
            window.location.href = "index.html";
        }, 1500);

    } catch (err) {
        error.innerText = "Server error";
    }
}



