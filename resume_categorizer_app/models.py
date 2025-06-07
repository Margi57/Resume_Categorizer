from django.db import models
from django.utils import timezone

class ResumeUpload(models.Model):
    file = models.FileField(upload_to='resumes/',null=True,blank=True) 
    file_name = models.CharField(max_length=255)
    extracted_text = models.TextField(blank=True)
    predicted_role = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(default=timezone.now)
    confidance_score = models.FloatField(blank=True)

    def _str_(self):
        return self.file_name