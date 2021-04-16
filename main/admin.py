from django.contrib import admin

# Register your models here.
from main.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id',
                  'name',
                  'family',
                  'title',
                  'body',
                  'created_at'
                    )
