# **FutureElevator-AI**
`FutureElevator-AI` is an innovative job-hunting application designed to revolutionize the way users find and apply for jobs globally. Utilizing advanced artificial intelligence, the platform enhances resumes, emails and cover letters tailored to individual job postings, ensuring candidates stand out in a competitive job market.

## **Features Of `FutureElevator-AI`:**

1. **User Authentication**: Users can log in using email and password.
2. **Platform Selection**: Users can select specific job platforms or choose to apply to all available platforms.
3. **Job Role and Date Filtering**: Users can specify job roles and filter job postings by posted date.
4. **Resume Upload**: Users can upload their resumes for processing.
5. **Resume Enhancement**: The application automatically enhances the user's resume based on the requirements of each job posting to ensure relevancy.
6. **Cover Letter Generation**: The application creates a tailored cover letter for each job application.
7. **Automated Job Applications**: Automatically applies to selected jobs, even redirecting to external websites as needed.
8. **Cold Email Sending**: Fetches company hiring emails and sends personalized cold emails to introduce the user for job opportunities.
9. **ATS Compliance Checking**: Checks the resume for ATS (Applicant Tracking System) compliance at various stages:
    - Before enhancing the resume.
    - After creating new resumes and cover letters.
    - While sending cold emails.
10. **CSV Data Export**: Allows users to download a CSV file containing job application data and information scraped from selected websites.
11. **Job Application Dashboard**: Provides a dashboard displaying:
    - Applied job
    - Accepted jobs
    - Rejected jobs
    - Detailed information about each job
    - Filtering options for easy navigation.
12. **Additional Features**: Ongoing development of more functionalities to enhance the job application process.

## **Project Structure**:

```bash
FutureElevator-AI/
│
├── README.md                    # Project documentation and overview
├── requirements.txt              # Python dependencies
├── package.json                  # React frontend dependencies
├── .gitignore                    # Files to ignore in version control
├── config.py                     # Configuration file (API keys, database URIs, etc.)
├── manage.py                     # Django command-line utility
├── pipelines/                    # Folder containing data pipelines and automation scripts
│   ├── __init__.py               # To make it a package
│   ├── data_ingestion.py         # Job data collection (API calls, web scraping)
│   ├── resume_parser.py          # Resume parsing and text extraction
│   ├── job_description_parser.py # Preprocessing job descriptions
│   ├── feature_engineering.py    # Feature engineering for job-resume matching
│   ├── ats_checker.py            # ATS compliance checking
│   ├── resume_enhancer.py        # NLP model to enhance resumes
│   ├── cover_letter_gen.py       # Cover letter generation model
│   ├── job_application.py        # Job application automation script (Selenium)
│   ├── cold_email.py             # Cold email automation script
│   └── dashboard_pipeline.py     # Data aggregation for the dashboard
│
├── src/                          # Core logic of the application (API, frontend, backend)
│   ├── backend/                  # Django backend logic
│   │   ├── FutureElevatorAI/     # Main Django app folder
│   │   │   ├── __init__.py       # Django project initialization
│   │   │   ├── settings.py       # Django project settings
│   │   │   ├── urls.py           # Application URL routing
│   │   │   ├── wsgi.py           # WSGI application entry point
│   │   ├── auth/                 # Authentication (login, signup)
│   │   │   ├── __init__.py       # Auth package initialization
│   │   │   ├── views.py          # Views for login and signup
│   │   │   ├── models.py         # Auth-related database models
│   │   │   ├── serializers.py    # Auth serializers (for request validation)
│   │   │   ├── urls.py           # Auth URL routing
│   │   ├── job_app/              # Main job application functionality
│   │   │   ├── __init__.py       # Package initialization
│   │   │   ├── views.py          # Views for job applications, resume upload
│   │   │   ├── models.py         # Database models for jobs, resumes
│   │   │   ├── serializers.py    # Data serializers for job apps
│   │   │   ├── urls.py           # URL routing for job application features
│   │   └── templates/            # Django HTML templates (if needed for some pages)
│   │       ├── layout.html       # Base layout template
│   │       ├── login.html        # Login page
│   │       ├── dashboard.html    # User dashboard page
│   │       └── apply_job.html    # Job application page
│   ├── frontend/                 # React frontend logic
│   │   ├── public/               # Public assets (index.html, favicon, etc.)
│   │   ├── src/                  # React application source code
│   │   │   ├── components/       # Reusable React components
│   │   │   │   ├── Auth/         # Login and signup forms
│   │   │   │   ├── Dashboard/    # User dashboard components
│   │   │   │   └── JobAppForm/   # Job application form components
│   │   │   ├── pages/            # Pages (e.g., Dashboard, Job Application, Login)
│   │   │   ├── services/         # API service to communicate with Django backend
│   │   │   └── App.js            # Main React app component
│   └── static/                   # Static files (CSS, JavaScript, images)
│       ├── css/                  # Custom CSS
│       └── js/                   # Custom JavaScript
│
├── models/                       # Machine learning models for ATS, resume enhancement
│   ├── __init__.py               # To make it a package
│   ├── ats_model.py              # ATS compliance model
│   ├── resume_enhancer_model.py  # NLP model for enhancing resumes
│   ├── cover_letter_model.py     # GPT model for cover letter generation
│   └── job_matching_model.py     # Model for job-resume matching
│
├── notebooks/                    # Jupyter notebooks for experiments
│   ├── EDA_resume_data.ipynb     # EDA for resume data
│   ├── EDA_job_description.ipynb # EDA for job description data
│   └── ats_model_experiments.ipynb # ATS compliance model experiments
│
├── data/                         # Data storage (raw, processed, and features)
│   ├── raw/                      # Raw data (scraped job listings, resumes)
│   ├── processed/                # Preprocessed data for machine learning models
│   ├── features/                 # Feature data (job-resume matching)
│   └── results/                  # Outputs (enhanced resumes, cover letters)
│
├── logs/                         # Log files for tracking execution of pipelines
│   ├── ingestion.log             # Log for job data ingestion
│   ├── resume_parser.log         # Log for resume parsing
│   ├── job_application.log       # Log for job application automation
│   └── ats_checker.log           # Log for ATS compliance checking
│
├── tests/                        # Unit and integration tests
│   ├── test_auth.py              # Tests for authentication module
│   ├── test_pipelines.py         # Tests for pipeline scripts
│   ├── test_models.py            # Tests for machine learning models
│   └── test_routes.py            # Tests for Django/React API routes
│
├── database/                     # Database scripts for PostgreSQL and MongoDB
│   ├── schema.sql                # SQL schema for PostgreSQL
│   ├── migrations/               # Django migrations for PostgreSQL
│   └── mongo_setup.py            # MongoDB connection and setup
│
└── deployment/                   # Deployment configuration and scripts
    ├── Dockerfile                # Dockerfile for building the app
    ├── docker-compose.yml        # Docker-Compose setup for multi-container development
    ├── nginx.conf                # Nginx configuration for serving the app
    └── deploy.sh                 # Deployment script (for cloud services like Heroku, AWS)

```

