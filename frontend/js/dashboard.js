window.onload = async function () {
    const token = localStorage.getItem("token");
    if (!token) {
        window.location.href = "index.html";
        return;
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/me", {
            method: "GET",
            headers: {
                "Authorization": "Bearer " + token
            }
        });

        const data = await res.json();

        if (!res.ok) {
            localStorage.removeItem("token");
            window.location.href = "index.html";
            return;
        }
        document.getElementById("name").innerText = data.user.full_name;
        document.getElementById("email").innerText = data.user.email;
        document.getElementById("role").innerText = data.user.role;

    } catch (err) {
        console.error(err);
        alert("Unable to load dashboard");
    }
};

function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}
