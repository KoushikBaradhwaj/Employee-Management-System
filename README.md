📁 Project Overview
This is a Flask-based web application for managing employees in a company. It supports basic operations such as:

Adding employees

Viewing employee records

Updating and deleting employee data

Assigning departments

The application uses MySQL Workbench as the database interface and runs entirely through Visual Studio Code.

🧾 Folder Contents
File/Folder	               Description
app.py	                       Entry point to start the Flask app
main.py	                       Initializes the application and configuration
routes.py	               Contains all route functions (e.g. add, view, update employees)
forms.py	               Manages all Flask-WTF forms (form validation)
models.py	               SQLAlchemy models representing database tables
add_initial_data.py	       Script to populate initial dummy data into the database
employeeDB.sql	               SQL file to create and structure the employee database
/static/	               Contains static files like CSS, JS, images
/templates/	               Jinja2 HTML templates for frontend rendering

🧰 Prerequisites
Before running the project, make sure the following tools and libraries are installed:

✅ Required Software:
Python (version 3.8 or higher)

MySQL Workbench

Visual Studio Code

pip (Python package manager)

Git (optional, for version control)

✅ Required Python Libraries:

Install the following packages using pip:

nginx
Copy
Edit
Flask
Flask-WTF
Flask-SQLAlchemy
mysql-connector-python

You can install all dependencies using:

nginx
Copy
Edit
pip install -r requirements.txt
Note: Create a requirements.txt file if not already present.

🧱 Database Setup (MySQL Workbench)

Open MySQL Workbench

Run the employeeDB.sql script to create the required database and tables.

You can also run add_initial_data.py to insert some sample data into the tables.

Ensure the database name, username, and password are correctly configured in your main.py or configuration file.

▶️ Running the Application

Open the folder in Visual Studio Code

Run the application with the command:

nginx
Copy
Edit
python app.py
Open your browser and go to:
http://127.0.0.1:5000/

You will see the homepage of the Employee Management System.

📌 Summary

Feature	Technology Used
Frontend	HTML, CSS (via Jinja templates)
Backend	Python (Flask)
Database	MySQL via MySQL Workbench
ORM	SQLAlchemy
Form Handling	Flask-WTF
IDE	Visual Studio Code

ℹ️ Notes

Make sure MySQL is running before starting the app.

Update database credentials in your configuration files if necessary.

Always use a virtual environment for dependency isolation.