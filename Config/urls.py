
from django.contrib import admin
from django.urls import path, include

# Создаем router и регистрируем наш ViewSet
from rest_framework import routers

from main.views import NoteViewSet

router = routers.SimpleRouter()
router.register('api/notes', NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),

]
# URLs настраиваются автоматически роутером
urlpatterns += router.urls