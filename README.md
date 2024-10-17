# Candidate: An Online CV Platform for Recruiters and Job Seekers


Welcome to Candidate, an online CV platform built to simplify the hiring process by allowing candidates to create their CVs directly on the platform, and recruiters to search and view these CVs without downloading any documents.

## Features
* Two Account Types: Candidate and Recruiter roles to streamline access.

* Interactive CV Creation: Candidates build CVs directly on the platform.

* Direct CV Viewing for Recruiters: No downloads required—CVs are viewable instantly.

* Search Functionality: Recruiters search candidates by career field and years of experience using filters.

* Profile Cards: Recruiter dashboard displays candidate summaries with profile pictures, experience, and fields.

* Easy Navigation: Intuitive dashboards and forms for smooth user interaction.

* Secure Account Management: Users can edit CVs, delete accounts, or log out seamlessly.

* Reliable Data Handling: PostgreSQL database ensures fast and secure storage of user data.

## How It Works
1. Sign-up Process
   * Users choose between two roles: Candidate or Recruiter.
2. For Candidates
   * Create an account and build a CV using an interactive form.
   * Upon login, candidates access the dashboard, which displays a preview of their CV and provides the following actions:
     * Edit CV: Modify the existing CV content.
     * Delete Account: Remove the account and data.
     * Logout: End the current session.
3. For Recruiters
   * After login, recruiters access the dashboard populated with candidate cards.
   * Each card shows the candidate's name, field, years of experience, and profile picture.
   * Recruiters can use the search bar to filter candidates by field and experience.
   * Clicking a candidate’s card takes the recruiter to the candidate's full CV, which includes contact information for easy outreach.

## Technologies Used
* Backend: Python’s Django framework
* Database: PostgreSQL for storing user profiles, CVs, and related data
* Frontend: HTML, CSS, JavaScript, and Bootstrap 5 for responsive design
* Search Functionality: Implemented with django-filter
* Deployment: Instructions for deployment are provided below

## Setup and Installation
### Prerquisites
* Python 3.x
* PostgreSQL
* Git

## Installation Steps
1. Clone the repository
   ```bash
   git clone https://github.com/Shayne999/Candidate2.0.git
   cd Candidate2.0
   cd candidate
   ```
2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Setup the PostgreSQL database
   * Create a PostgreSQL database. Update the database settings in settings.py:
   ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your_database_name>',
        'USER': 'postgres',
        'PASSWORD': '<your_password>',
        'HOST': 'localhost',
        'PORT': '5432',
            }
    }
    ```
5. Apply migrations
   ```bash
   python manage.py migrate
    ```
6. Create a superuser (for admin access)
   ```bash
   python manage.py createsuperuser
    ```
7. Run the development server
   ```bash
   python manage.py runserver
    ```
8. Open your browser and navigate to http://localhost:8000.

## Usage
* Candidate Registration: Create a candidate account and build a CV.
* Recruiter Login: Access candidate profiles, search for talent, and view full CVs.
* Edit CV: Candidates can update their profiles anytime.
* Search and Filter: Recruiters use filters to find relevant candidates.
* No CV Downloads: Recruiters view CVs directly within the platform.

## Known Issues
* Deployment Challenges: Proper PostgreSQL configuration is required for cloud deployment.
* Email Notification System: Future versions may implement notifications for candidate-recruiter interactions.

## Future Improvements
* Email/Message Notifications: Notify candidates when a recruiter views their profile.
* Profile Recommendations: Suggest relevant candidates based on recruiter preferences.
* Analytics Dashboard: Provide recruiters with metrics on candidate engagement.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name.

2. Commit your changes: git commit -m 'Add your feature'.

3. Push to the branch: git push origin feature/your-feature-name.

4. Create a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Images



![Screenshot (29)](https://github.com/user-attachments/assets/8bb1abf7-bbbe-4b93-bbb6-96052ed2c01e)

![Screenshot (25)](https://github.com/user-attachments/assets/28e1c595-7061-4e75-8e2d-88680b5bdefd)

![Screenshot (28)](https://github.com/user-attachments/assets/781ca174-ab1b-42b9-bbf7-186f36382ae8)




