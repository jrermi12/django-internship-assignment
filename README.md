# django-internship-assignment
Additional Instructions and Notes on Implementation Choices
1. Use of Django’s Built-in Authentication System

The project leverages Django's robust, built-in authentication system for user management. This approach ensures the security of user data and reduces implementation complexity while adhering to best practices. Specific features like login, password reset, and password change use Django’s default views and forms for consistency and reliability.
2. Form Handling and Validation

All forms in the application use Django’s form classes (AuthenticationForm, UserCreationForm, PasswordChangeForm, etc.). This ensures proper validation for fields like email, username, and password, reducing the risk of errors and ensuring user inputs meet security standards.
3. Email-Based Password Reset

The password reset functionality is implemented using Django’s built-in system for sending password reset emails. To test this feature, configure the email backend in settings.py. By default, the project uses Django’s console email backend to display email content in the terminal. Update the email settings with real SMTP credentials if live email functionality is needed.
4. Role-Based Page Access

Protected pages (e.g., Dashboard, Change Password, and Profile) are secured using Django’s @login_required decorator. This ensures only authenticated users can access these pages, meeting the assignment's requirement for restricted access.
5. URL Structure

The application uses a modular URL structure, with routes defined in the accounts/urls.py file for better maintainability. All major views (login, signup, dashboard, etc.) are mapped to intuitive URLs, making the application user-friendly.
6. Responsive and Minimal Design

Although styling is not a criterion for evaluation, the templates are structured with semantic HTML and basic Bootstrap classes

# How to run the Project

## Installation

1. Clone the repository:

2. Install Django:

    - On Windows:
        ```sh
        pip install django
        ```

    - On Linux:
        ```sh
        pip3 install django
        ```

3. Apply migrations:
    ```sh
    python3 manage.py migrate
    ```

4. Run the server:
    ```sh
    python3 manage.py runserver
    ```
    Or to specify a port:
    ```sh
    python3 manage.py runserver <port>
    ```
