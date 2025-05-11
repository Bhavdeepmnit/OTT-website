🎬 OTT Platform Website
This is a basic OTT (Over-The-Top) platform website built using Django, with HTML/CSS for frontend styling. The application is connected locally to a MySQL server for database management and includes fundamental features such as user login, sign-up, and feedback submission.

🚀 Features
🔐 User Authentication (Sign Up / Login)

💬 Feedback Submission Form

🎨 Frontend designed with HTML & CSS

🗃️ MySQL database integration

⚙️ Fully functional using Django backend

📦 Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS

Database: MySQL (local connection)

🔧 Installation and Setup
1. Clone the repository
git clone https://github.com/your-username/ott-website.git
cd ott-website


3. Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate     # On Windows use: venv\Scripts\activate


4. Install dependencies
pip install -r requirements.txt
(Make sure to generate requirements.txt using pip freeze > requirements.txt if not already present.)


5. Configure MySQL database
Update your settings.py file with your local MySQL database credentials:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Apply migrations
python manage.py migrate


7. Run the development server
python manage.py runserver


Visit http://127.0.0.1:8000 in your browser to view the website.

