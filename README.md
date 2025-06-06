# Resume_Categorizer

A Django-based web application that allows users to upload resumes (PDF or DOCX), extracts the text content, and categorizes the resumes into relevant job roles such as Frontend Developer, Backend Developer, Data Scientist, DevOps Engineer, UI/UX Designer, or Other.

---

## Features

- **File Upload:** Upload resumes in PDF or DOCX formats.
- **Text Extraction:** Extracts text from resumes using PyPDF2 and python-docx.
- **Role Classification:** Classifies resumes based on keyword rules or optionally with ML models.
- **Database Storage:** Saves filename, extracted text, predicted role, and upload timestamp in PostgreSQL.
- **Results Display:** Lists uploaded resumes with their predicted job roles.
- **Optional:** Search/filter resumes by category, download uploaded resumes, and confidence score display.

---

## Technologies & Libraries

- Python 3.x
- Django Web Framework
- PostgreSQL Database
- PyPDF2 (for PDF text extraction)
- python-docx (for DOCX text extraction)
- Scikit-learn or NLTK (optional, for ML-based classification)

---

## Installation & Setup Guide

### Prerequisites

- Python 3.x installed
- PostgreSQL installed and running
- Git installed (optional)

---

### Steps

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd <project-folder>
