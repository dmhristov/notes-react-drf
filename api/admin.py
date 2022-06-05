from django.contrib import admin
from api.models import Note

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    pass
