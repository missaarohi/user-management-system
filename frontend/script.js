async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email: email,
      password: password
    })
  });

  const data = await res.json();
  console.log(data);

  if (res.ok) {
    localStorage.setItem("token", data.token);
    document.getElementById("result").innerText = "Login success";
  } else {
    document.getElementById("result").innerText = data.error;
  }
}
