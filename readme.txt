phones range - 



https://task-hero-y3xq.onrender.com
# TaskHero 🦸‍♂️📝

**TaskHero** is a task management web application built with Django. It helps users efficiently manage their daily tasks with clear organization, prioritization, and user-specific access. This app supports user authentication, task CRUD operations, and a clean, responsive dashboard UI.

---

## 🚀 Features

### 🔐 User Authentication
- Sign Up, Log In, and Log Out using Django’s built-in authentication.
- Sign-up form includes: first name, last name, email, username, password1, and password2.
- Authenticated users are redirected to their dashboard after login.
- Only authenticated users can access the task dashboard and perform task operations.

### 🗂️ Task Management (CRUD)
#### Create
- Users can add tasks with:
  - **Title**
  - **Description**
  - **Due Date**
  - **Status**: To Do, In Progress, Completed
  - **Priority**: Low, Medium, High

#### Read
- Dashboard displays tasks grouped into three columns based on status:
  - **To Do**
  - **In Progress**
  - **Completed**
- Each task is presented in a card with:
  - Title
  - Due Date
  - Priority (Color-coded)
  - **Overdue** tag if past due
  - Edit & Delete buttons

#### Update
- Tasks can be edited by clicking the "Edit" button on the task card or detail page.

#### Delete
- Tasks can be deleted after a confirmation prompt.

### 👤 User-Specific Access
- Each user can only view, update, and delete their own tasks.
- Unauthorized access to other users’ tasks is restricted and safely handled.

### 🎨 UI & Design
- Clean, responsive layout
- Navigation bar with links to:
  - Home / Landing Page
  - Sign Up / Log In
- Dashboard card layout grouped by task status
- Overdue tasks are highlighted in red
- Color-coded priority labels:
  - 🔴 High
  - 🟡 Medium
  - 🔵 Low

---

## 📄 Pages

- **Landing Page**: Brief overview of TaskHero with a call to action to sign up.
- **Authentication Pages**: Sign Up, Log In, Log Out
- **Dashboard**: Task management area (grouped cards, search, and filters)
- **Task Detail Page**: Full view of a single task with edit and delete options
- **Add Task Page**: Form for creating a new task
- **Edit Task Page**: Form for updating an existing task
- **Delete Confirmation Page**: Prompt to confirm task deletion

---

## 🔐 Permissions

- Only logged-in users can:
  - Create tasks
  - View their dashboard
  - Edit their own tasks
  - Delete their own tasks
- Attempting to access or edit another user's tasks will redirect the user or display a permission-denied message.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3 (custom styling)
- **Database**: SQLite (default) or MySQL (configurable)
- **Authentication**: Django’s built-in system

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ouckland/Task-Hero.git
   cd taskhero
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database in `settings.py`**
   (Use SQLite by default or configure MySQL)

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

6. **Access**
   - Open in browser: `http://127.0.0.1:8000/`

---

## 📬 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
