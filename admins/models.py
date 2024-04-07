# models.py in the admins app
from django.db import models

class UserExperience(models.Model):
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.experience[:50]  # Display first 50 characters of experience
