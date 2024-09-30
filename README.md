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
├── README.md                             # Project documentation and overview
├── requirements.txt                      # List of dependencies for Django
├── package.json                          # List of dependencies for React
├── .gitignore                            # Files to ignore in version control
├── config.py                             # Configuration file (e.g., API keys, database URIs)
│
├── pipelines/                            # Folder containing data pipelines and automation scripts
│   ├── __init__.py                       # To make it a package
│   ├── data_ingestion.py                 # Job data collection (API calls, web scraping)
│   ├── resume_parser.py                  # Preprocessing resumes (NLP)
│   ├── job_description_parser.py          # Preprocessing job descriptions
│   ├── feature_engineering.py            # Feature creation for resume/job matching
│   ├── ats_checker.py                    # ATS compliance checking pipeline
│   ├── resume_enhancer.py                # NLP model for enhancing resumes
│   ├── cover_letter_gen.py               # Cover letter generation model
│   ├── job_application.py                 # Web automation script (Selenium)
│   ├── cold_email.py                     # Cold email automation script
│   └── dashboard_pipeline.py              # Data aggregation for dashboard
│
├── src/                                  # Core logic of the application (API, frontend, backend)
│   ├── backend/                          # Django backend code
│   │   ├── manage.py                     # Django management script
│   │   ├── FutureElevatorAI/             # Django project folder
│   │   │   ├── __init__.py                # Initialization file
│   │   │   ├── settings.py                # Django settings
│   │   │   ├── urls.py                    # URL routing
│   │   │   ├── wsgi.py                    # WSGI entry point
│   │   │   ├── asgi.py                    # ASGI entry point for async support
│   │   │   ├── auth/                      # Authentication app
│   │   │   │   ├── __init__.py
│   │   │   │   ├── views.py               # View functions for authentication
│   │   │   │   ├── models.py              # Models for user authentication
│   │   │   │   └── serializers.py         # Serializers for API responses
│   │   │   ├── job_application/           # Job application app
│   │   │   │   ├── __init__.py
│   │   │   │   ├── views.py               # Job application logic
│   │   │   │   ├── models.py              # Job application models
│   │   │   │   └── serializers.py         # Serializers for job applications
│   │   │   └── pipelines/                 # Pipeline scripts specific to backend
│   │   └── requirements.txt               # Python dependencies
│   │
│   ├── frontend/                          # React frontend code
│   │   ├── public/                        # Public assets (index.html, images, etc.)
│   │   ├── src/                           # Source files for React components
│   │   │   ├── components/                # Reusable React components
│   │   │   │   ├── Auth/                  # Authentication components (Login, Signup)
│   │   │   │   ├── Dashboard/              # Dashboard components
│   │   │   │   └── JobApplication/        # Job application components
│   │   │   ├── App.js                     # Main application component
│   │   │   ├── index.js                   # Entry point for React
│   │   │   └── api.js                     # API service for backend integration
│   │   └── package.json                   # NPM dependencies
│   │
│   ├── models/                            # Contains machine learning models and preprocessing logic
│   │   ├── __init__.py                    # To make it a package
│   │   ├── ats_model.py                   # ATS compliance model (classifier)
│   │   ├── resume_enhancer_model.py       # NLP model to enhance resumes
│   │   ├── cover_letter_model.py          # Model for cover letter generation
│   │   └── job_matching_model.py           # Model for job-resume matching
│   │
│   ├── notebooks/                         # Jupyter notebooks for experimentation, EDA, and prototyping
│   │   ├── EDA_resume_data.ipynb          # Exploratory data analysis of resumes
│   │   ├── EDA_job_description.ipynb       # EDA of job descriptions
│   │   └── ats_model_experiments.ipynb     # ATS model training experiments
│   │
│   ├── data/                              # Data storage (raw, processed, and features)
│   │   ├── raw/                           # Raw data collected from scraping/APIs
│   │   │   ├── job_listings.json          # Raw job listing data (scraped/API)
│   │   │   ├── resumes/                   # Uploaded resumes (before preprocessing)
│   │   ├── processed/                     # Preprocessed data ready for modeling
│   │   │   ├── resume_text.csv            # Preprocessed resume data
│   │   │   ├── job_description.csv         # Cleaned job descriptions
│   │   └── features/                      # Feature data for models
│   │       ├── resume_features.csv        # Features extracted from resumes
│   │       └── job_matching_features.csv    # Matching features between resumes & jobs
│   │
│   ├── logs/                              # Application and pipeline logging for debugging
│   │   ├── ingestion.log                  # Logs for data ingestion pipeline
│   │   ├── resume_parser.log              # Logs for resume parsing pipeline
│   │   ├── job_application.log            # Logs for job application automation
│   │   └── ats_checker.log                # Logs for ATS compliance checker
│   │
│   ├── tests/                             # Unit and integration tests for all components
│   │   ├── test_auth.py                   # Tests for authentication
│   │   ├── test_pipelines.py              # Tests for pipeline functions
│   │   ├── test_models.py                 # Tests for models (ATS, resume enhancer)
│   │   └── test_routes.py                 # Tests for Django routes
│   │
│   ├── database/                          # Database scripts and models
│   │   ├── schema.sql                     # SQL schema for relational database (PostgreSQL)
│   │   ├── migrations/                    # Database migration files (e.g., Alembic for Flask)
│   │   └── database_config.py             # Configurations for connecting to the database
│   │
│   └── deployment/                        # Deployment scripts and Docker setup
│       ├── Dockerfile                     # Dockerfile for containerization
│       ├── docker-compose.yml             # Docker-compose for multi-container setup
│       ├── setup.sh                       # Shell script to set up the environment
│       ├── nginx.conf                     # Nginx configuration for serving the app
│       └── deploy_to_aws.sh               # Script for deploying to AWS (or GCP/Heroku)
│
└── .env                                   # Environment variables (e.g., API keys, database URIs)

```