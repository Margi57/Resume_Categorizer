# Resume Categorizer - Django ML App

A Django web application that classifies uploaded resumes into job roles using a machine learning model (Random Forest). This tool helps categorize resumes such as Backend Developer, Data Scientist, QA Tester, etc., based on their content.

## 🔧 Features

* Upload resumes in PDF or DOCX format
* Text extraction and preprocessing
* Job role prediction using trained ML model
* Displays confidence scores
* Resume history listing

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Margi57/Resume_Categorizer.git
cd Resume_Categorizer
```

### 2. Create Environment (Recommended)

```bash
conda create -n resume_detect_env python=3.10
# Activate the environment:
conda activate resume_detect_env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Make Migrations and Migrate

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Access the App

```
http://127.0.0.1:8000/
```

* Upload Page: `/`
* Resume List: `/resumes/`

---

## 📍 URL Overview

| URL         | View Function   | Description           |
| ----------- | --------------- | --------------------- |
| `/`         | `upload_resume` | Upload resume         |
| `/resumes/` | `list_resumes`  | List uploaded resumes |
| `/admin/`   | Django Admin    | Admin panel           |

---

## 🧠 Machine Learning Model

* Model: `LogisticRegression`
* Vectorizer: `TfidfVectorizer`
* Stored at: `Resume_Categorizer\model.pkl`
* Trained on skill-based synthetic resume data
* Returns top job role with confidence

---

## ⚠️ Notes

* Ensure `media/` directory exists and is writable
* Run `python manage.py createsuperuser` to access admin panel
* Retrain and overwrite the `.pkl` file to improve accuracy

---

