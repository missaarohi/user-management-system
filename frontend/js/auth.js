async function login() {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    const error = document.getElementById("error");
    error.innerText = "";

    if (!email || !password) {
        error.innerText = "Email and password required";
        return;
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email,
                password
            })
        });

        const data = await res.json();

        if (!res.ok) {
            error.innerText = data.error || "Invalid credentials";
            return;
        }

        localStorage.setItem("token", data.token);
        window.location.href = "dashboard.html";

    } catch (err) {
        error.innerText = "Server error";
    }
}
