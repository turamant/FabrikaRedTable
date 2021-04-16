from django.urls import path

from main.views import HomeView, notes_page, notes_app

urlpatterns = [
    path('',notes_page, name='notes'),
    path('notes_app/',notes_app, name='notes_app')

]

