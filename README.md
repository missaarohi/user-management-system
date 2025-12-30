# User Management System (Backend + Frontend)

A complete **User Management System** built using **Flask (Python)** and **MongoDB**, with authentication, role-based access, and a simple frontend UI for signup, login, and dashboard.


---

## 🚀 Features

### 🔐 Authentication
- User Signup
- User Login
- Password hashing using **bcrypt**
- JWT-based authentication

### 👥 User Roles
- Default role: `user`
- Supports role-based access (e.g. admin, user)
- Role is stored and returned from backend

### 📊 Dashboard
- Displays logged-in user details:
  - Name
  - Email
  - Role
- Logout functionality

### 🛡 Protected Routes
- `/me` endpoint accessible only with valid JWT token

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- MongoDB (MongoDB Atlas)
- Flask-PyMongo
- JWT (PyJWT)
- bcrypt

### Frontend
- HTML
- CSS
- JavaScript (Vanilla JS)
- Fetch API for backend integration

---
