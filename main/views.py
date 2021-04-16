from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Note
from .serializers import NoteSerializer
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

def notes_page(request):
    return render(request, 'notes.html',{'notes':Note.objects.all()})

def notes_app(request):
    return render(request,'notes_app.html')