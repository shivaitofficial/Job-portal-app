
# 💼 Job Portal Application

A full-stack Job Portal web application built using **Django (Backend)** and **React (Frontend)**.  
This platform allows users to explore jobs, apply for positions, and manage applications efficiently.

## 🚀 Features

### 👤 Authentication
- User login & registration
- Session handling
- Secure API communication

### 💼 Job Management
- View available job listings
- Job details page
- Apply for jobs
- Prevent duplicate applications

### 📄 Application System
- Apply to jobs with one click
- Track application status
- Status updates (Pending, Shortlisted, Rejected, Hired)

### 🎨 Frontend
- Responsive UI using React + Tailwind CSS
- Smooth navigation using React Router
- Real-time feedback messages


## 🛠️ Tech Stack

### 🔹 Backend
- Django
- Django REST Framework (DRF)
- SQLite / PostgreSQL

### 🔹 Frontend
- React.js
- Tailwind CSS
- React Router

---

## 📂 Project Structure
JobPortal/
│
├── backend/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
│ └── db.sqlite3
│
├── frontend/
│ ├── src/
│ │ ├── pages/
│ │ ├── components/
│ │ └── App.js
│
└── README.md

---

## ⚙️ Installation & Setup

### 🔧 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
👉 Backend runs at: http://127.0.0.1:8000/

💻 Frontend Setup
cd frontend
npm install
npm start

👉 Frontend runs at: http://localhost:3000/
🔗 API Endpoints
Method	Endpoint	Description
POST	/login/	User login
GET	/job/	Get all jobs
POST	/apply/	Apply for a job

📌 Future Enhancements
JWT Authentication
Resume upload feature
Admin dashboard
Email notifications
Job filtering & search

👨‍💻 Author
Sivakumar Selvam
