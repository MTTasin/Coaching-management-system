# Coaching Management System Web Application

This is a web application that allows coaching centers to manage their students, teachers, payments, and attendance. It is built with Bootstrap, HTML, CSS, and Django.

***Point to be noted before you copy-paste all of it. I have removed my security key from the settings.py of the project. As it is an actual project that I have built for my client. So it will not run if you run directly. You have to generate a security key before you do so.***

You can check this project here [Live website](https://shikkhashala.com/)

## Features

- Adding new students
- Managing the students
- Adding payment options
- Student will be able to download the payment slip from their profile page
- Add student attendance
- Students will be able to see their attendance on their student profile
- Add teachers
- Teacher will be able to add attendance of the students of their class
- Teacher can upload the topic of the class which will show in the student’s profile according to their class

## Installation

To install and run this project, you need to have Python 3 and Django installed on your system. You also need to have a database server such as MySQL or PostgreSQL.

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages using `pip install -r requirements.txt`.
4. Create a database and a user for the project, and grant all privileges to the user.
5. Edit the `settings.py` file and change the database settings according to your database server and credentials. Note: the security key has been removed from the `settings.py` file for security reasons. You need to generate a new one and add it to the file.
6. Run `python manage.py migrate` to create the database tables.
7. Run `python manage.py createsuperuser` to create an admin user for the project.
8. Run `python manage.py runserver` to start the development server.

## Usage

To use the web application, you need to open your browser and go to the URL of the development server, such as `http://127.0.0.1:8000/`.

- To access the admin panel, you need to go to `http://127.0.0.1:8000/admin/` and log in with your admin credentials.


## Credits

This project was developed by MTTasin(https://github.com/MTTasin) for any queries or feedback.



