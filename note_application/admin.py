from django.contrib import admin
from .models import Note, Share, NoteUpdateAttempt

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'owner']
    list_filter = ['owner','id']  
    search_fields = ['title', 'content', 'owner__username', 'id']  

@admin.register(NoteUpdateAttempt)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'user','note_id','timestamp']
    list_filter = ['user','id','note_id','timestamp'] 
    search_fields = ['title', 'content', 'user', 'id','note_id','timestamp'] 

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ['id', 'note_id', 'user_id']
    list_filter = ['note_id', 'user_id','id']
    search_fields = ['note_id', 'user_id','id']
