# 🦸‍♂️ TaskHero — Smart Task Manager

🔗 **Live Demo:** [https://task-hero-y3xq.onrender.com](https://task-hero-y3xq.onrender.com)

---

**TaskHero** is a sleek and intuitive **task management web app** built with **Django**.  
It helps users organize, prioritize, and manage daily tasks efficiently — with secure user authentication and a responsive, dashboard-based UI.

---

## 🚀 Features

### 🔐 Authentication
- Sign up, log in, and log out using Django’s authentication system.  
- Sign-up fields: `first name`, `last name`, `email`, `username`, `password`.  
- Authenticated users are redirected to their personal dashboard.  
- Non-authenticated users cannot access task management pages.

### ✅ Task Management (CRUD)
#### Create
Add tasks with:
- **Title**
- **Description**
- **Due Date**
- **Status** → To-Do, In Progress, Completed
- **Priority** → Low, Medium, High

#### Read
- Dashboard groups tasks into 3 columns by status:
  - 🧩 *To Do*
  - 🚧 *In Progress*
  - 🏁 *Completed*
- Each task card shows:
  - Title, Due Date, Priority (color-coded)
  - “Overdue” tag if past due
  - Edit & Delete buttons

#### Update / Delete
- Edit tasks directly from the dashboard.  
- Delete tasks with confirmation prompts.  

### 👤 User-Specific Access
- Each user sees only their own tasks.  
- Any unauthorized access attempt is safely blocked.

### 🎨 UI / UX
- Clean, responsive design  
- Navigation bar with Home, Sign Up, and Login  
- Color-coded priorities:
  - 🔴 High
  - 🟡 Medium
  - 🔵 Low
- Overdue tasks highlighted in red

---

## 🗂️ Pages Overview

| Page | Description |
|------|--------------|
| **Landing Page** | Overview of TaskHero with Sign Up CTA |
| **Sign Up / Login / Logout** | Auth pages for users |
| **Dashboard** | Task overview with status columns |
| **Task Detail** | View, edit, or delete a single task |
| **Add Task** | Form to create new tasks |
| **Edit Task** | Update existing tasks |
| **Delete Confirmation** | Safe delete confirmation prompt |

---

## 🔐 Permissions

- Only logged-in users can **create, view, update, or delete** their own tasks.  
- Unauthorized access to another user’s task → Redirect or “Permission Denied”.

---

## 🛠️ Tech Stack

| Layer | Technology |
|--------|-------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML5, CSS3 |
| **Database** | SQLite (default) / MySQL (optional) |
| **Auth System** | Django built-in authentication |

---

## ⚙️ Setup Instructions

```bash
# 1️⃣ Clone the repo
git clone https://github.com/Ouckland/Task-Hero.git
cd Task-Hero

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Apply migrations
python manage.py migrate

# 4️⃣ Run the server
python manage.py runserver
