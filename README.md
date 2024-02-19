# Coaching Management System Web Application

This is a web application that allows coaching centers to manage their students, teachers, payments, and attendance. It is built with Bootstrap, HTML, CSS, and Django.

***Point to be noted before you copy-paste all of it. I have removed my security key from the settings.py of the project. As it is an actual project that I have built for my client. So it will not run if you run directly. You have to generate a security key before you do so.***

You can check this project here [Live website](https://shikkhashala.com/)

## Screenshot's
![1](https://github.com/MTTasin/Coaching-management-system/assets/153354819/4d373803-8ad4-4c43-b5f4-86f3605f1d74)
![course_details_page](https://github.com/MTTasin/Coaching-management-system/assets/153354819/aa6b21ce-d4f0-40c6-97f7-4cdd1b24038a)
![course_enroll_page](https://github.com/MTTasin/Coaching-management-system/assets/153354819/777ef667-130c-47ca-8f31-128d6aac37ea)
![contact_us](https://github.com/MTTasin/Coaching-management-system/assets/153354819/bd2cd034-1222-4308-9e09-6bc8db2533b2)
![gallery_page](https://github.com/MTTasin/Coaching-management-system/assets/153354819/05c495b2-4e98-497d-8c9d-933d90f09ee5)
![login_page](https://github.com/MTTasin/Coaching-management-system/assets/153354819/5aa9dbb7-c587-4a5e-9a16-b11ac48ba107)
![responsive](https://github.com/MTTasin/Coaching-management-system/assets/153354819/fe5362ff-d941-40bf-ac52-3a1013e4f451)
![studnets_profile](https://github.com/MTTasin/Coaching-management-system/assets/153354819/17ffe5b2-57ca-493c-a5b1-f3ac111b4aa7)
![teachers_profile](https://github.com/MTTasin/Coaching-management-system/assets/153354819/6f7449dd-3ef7-4e18-8fa5-ca54eaf7fbca)
![Uploading_class_topic](https://github.com/MTTasin/Coaching-management-system/assets/153354819/fc05a33e-c23c-4560-916e-311f91abc86c)




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



