import os
import PyPDF2
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    if ext == '.pdf':
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ''
    elif ext == '.docx':
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + '\n'
    return text.lower()

def classify_resume(text):
    roles = {
        'Frontend Developer': ['html', 'css', 'javascript', 'react', 'angular'],
        'Backend Developer': ['java', 'spring', 'django', 'flask', 'node.js'],
        'Data Scientist': ['machine learning', 'pandas', 'numpy', 'data analysis', 'tensorflow'],
        'DevOps Engineer': ['docker', 'kubernetes', 'aws', 'jenkins', 'ci/cd'],
        'UI/UX Designer': ['figma', 'adobe xd', 'wireframe', 'prototyping']
    }
    for role, keywords in roles.items():
        for keyword in keywords:
            if keyword in text:
                return role
    return 'Other'