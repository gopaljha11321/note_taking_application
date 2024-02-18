from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'owner']
    list_filter = ['owner','id']  # You can include other fields here for filtering, but 'id' is not necessary
    search_fields = ['title', 'content', 'owner__username', 'id']  # Search fields for searching by title, content, or owner username
