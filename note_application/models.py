from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    id = models.AutoField(primary_key=True)  # Ensure id is a primary key
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class NoteUpdateAttempt(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with the User model
    note_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    
class Share(models.Model):
    id = models.AutoField(primary_key=True)
    note_id = models.IntegerField() 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with the User model
