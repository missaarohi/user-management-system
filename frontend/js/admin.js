const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "login.html";
}

async function loadUsers() {
    const res = await fetch("http://127.0.0.1:5000/admin/users", {
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    if (res.status === 403) {
        document.body.innerHTML = "<h2>Access Denied</h2>";
        return;
    }

    const data = await res.json();
    const tbody = document.querySelector("#usersTable tbody");

    data.users.forEach(user => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${user.full_name}</td>
            <td>${user.email}</td>
            <td>${user.role}</td>
            <td>${user.status}</td>
        `;
        tbody.appendChild(row);
    });
}

function logout() {
    localStorage.clear();
    window.location.href = "login.html";
}

loadUsers();
