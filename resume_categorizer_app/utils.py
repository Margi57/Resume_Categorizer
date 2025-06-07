import os
import PyPDF2
import docx
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

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


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # remove punctuation/numbers
    text = re.sub(r'\s+', ' ', text)          # remove extra spaces
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    text = ' '.join(
        [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]
    )
    return text