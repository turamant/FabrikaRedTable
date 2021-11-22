# Create your models here.

from django.db import models
class Note(models.Model):
    name = models.CharField(max_length=40, null=True,default='Name')
    family = models.CharField(max_length=60, null=True, default='Family')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        #Вычисляемое поле full_name
        return ' '.join([self.family, self.name]).capitalize()
