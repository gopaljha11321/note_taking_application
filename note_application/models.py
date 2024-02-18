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
    
class Share(models.Model):
    id = models.AutoField(primary_key=True)
    note_id = models.IntegerField()  # Adjust this according to your requirements
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with the User model
