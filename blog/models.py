from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization ', 'Immunization '),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='accounts/profile/static/local-cdn',blank=True, null=True)
    Category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    Summary = models.TextField()
    Content = models.TextField()
    is_draft = models.BooleanField(default=False)

