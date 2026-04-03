🧠 Habit Tracker with Analytics

📌 Overview

This is a Python + MySQL based Habit Tracker System that allows users to manage daily habits and track their progress over time.

---

🚀 Features

- 🔐 User Registration & Login
- ➕ Add New Habits
- 📋 View Habits
- ✅ Mark Habit as Done/Missed
- 📊 View Progress / Analytics
- ❌ Delete Habit

---

🛠️ Technologies Used

- Python
- MySQL
- MySQL Connector

---

🗂️ Database Structure

1. USERS

- user_id (Primary Key)
- username
- password

---

2. HABITS

- habit_id (Primary Key)
- user_id (Foreign Key)
- habit_name
- created_at (Date)

---

3. LOGS

- log_id (Primary Key)
- habit_id (Foreign Key)
- created_at (Date) (Foreign key)
- status (Done / Missed)

---

⚙️ How to Run the Project

1. Install required library:

pip install mysql-connector-python

2. Create database:

CREATE DATABASE habit_tracker;

3. Create tables using SQL queries.

4. Update credentials:

host="localhost"
user="root"
password="YOUR_PASSWORD"
database="habit_tracker"

5. Run:

python main.py

---

🔒 Security Note

Database credentials are not included. Use your own credentials.

---

🎯 Future Improvements

- 🔥 Streak tracking
- 📊 Graph analytics
- ⏰ Reminder system
- 💻 GUI / Web version

---

👩‍💻 Author

Bhumi Pathak
