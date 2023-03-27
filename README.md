# Backend-CA1

Dorset College Backend Course | Assesment #1


# What is this project about ?

This project aims to provide users with a virtual garage in which they can register their motorcycles by name, brand, and description. The primary purpose of this project is to offer a simple and efficient way for users to keep track of their motorcycle collection.
In a second time, this projects aims to include a registration system.

# Detail

To access to the garage, we have to log in. (If you want to try it, login: admin - password: administrator).
When we are logged in, we can log out, reset the password or connect to the garage.
On the main page, you can see the different motorcycles, edit them on the left, and delete them on the right. A navigation bar at the top allows you to return to this page or add a motorcycle.
When you click on a motorcycle, you access its description and can still edit it from there.
In the edit, delete or create pages, you see a form for the respective motorcycle with a confirmation button.
To finish, it is possible to log out directly from the garage with the navigation bar on top of the screen.

# Testing

This repository contains the tests for the views.py and models in the garage app. The purpose of this test suite is to ensure that the functionalities implemented in the views and models are working as expected.
The file tests.py is used to test the model and the file tests_views.py is used to ensure that the views are working well.

# Anti-Hack for CSS and Redirection

In addition to the tests for views.py and models, we have also implemented an anti-hack mechanism to prevent CSS attacks and unauthorized redirections in our Django project.

The anti-hack mechanism works by validating the input data received from the user before processing it. This validation ensures that the input data does not contain any malicious code or commands that could compromise the security of the system.

# What are the limitations ?

Currently, the application lacks the ability to share opinions on motorcycles or filter motorcycles by brand. These limitations may impact the user experience for those looking for specific types of motorcycles or seeking to engage with other users about their shared interests.


# What can be improved in the future ?

In the future, I plan to implement a new class to allow each user to add opinions on a registered motorcycle. Additionally, I aim to add motorcycle categories to the application, which will enable users to filter their collection based on their specific interests. Another possible improvement could be to integrate a search function to make it easier for users to find specific motorcycles within their collection.


# How did I process ?

The development process began by creating the "garage" application and implementing the primary model to enable motorcycle registration. The next step involved adding CRUD functions to the application, followed by the development of HTML templates and CSS to enhance the user experience and overall look and feel of the application. To ensure the application is secure, I added user authentication and authorization features to protect user data. Finally, I conducted extensive testing to ensure the application functions correctly and is free of bugs and errors.

Github : git@github.com:ErwannLesech/Backend-CA1.git

LESECH Erwann