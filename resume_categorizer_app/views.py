import os
import datetime
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import ResumeUpload
from .forms import ResumeUploadForm
from .utils import extract_text_from_file, classify_resume
from .role_detectore import predict_role

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['resume']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_path = fs.path(filename)

            # Extract text
            text = extract_text_from_file(file_path)
            print("text====>",text)
            # Classify role
            role = predict_role(text)
            print(role)

            # Save to DB
            resume = ResumeUpload(
                file=file,
                file_name=filename,
                extracted_text=text,
                predicted_role=role[0],
                uploaded_at=datetime.datetime.now(),
                confidance_score = 1
            )
            resume.save()
            return redirect('list_resumes')
    else:
        form = ResumeUploadForm()
    return render(request, 'upload_resume.html', {'form': form})


def list_resumes(request):
    resumes = ResumeUpload.objects.all().order_by('-uploaded_at')
    return render(request, 'resume_list.html', {
        'resumes': resumes,
        'MEDIA_URL': settings.MEDIA_URL
    })