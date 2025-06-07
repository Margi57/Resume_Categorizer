import os
import datetime
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import ResumeUpload
from .forms import ResumeUploadForm
from .utils import extract_text_from_file
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
            # Predict role 
            predicted_role, confidence_score = predict_role(text)
            
            resume = ResumeUpload(
                file=file,
                file_name=filename,
                extracted_text=text,
                predicted_role=predicted_role,
                uploaded_at=datetime.datetime.now(),
                confidance_score = confidence_score
            )
            resume.save()
            return redirect('list_resumes')
    else:
        form = ResumeUploadForm()
    return render(request, 'upload_resume.html', {'form': form})


def list_resumes(request):
    query = request.GET.get('query')
    if query:
        resumes = ResumeUpload.objects.filter(predicted_role__icontains=query).order_by('-uploaded_at')
    else:
        resumes = ResumeUpload.objects.all().order_by('-uploaded_at')
    return render(request, 'resume_list.html', {
        'resumes': resumes,
        'MEDIA_URL': settings.MEDIA_URL,
        'query': query or ''
    })