from django.db import models
from src.core.models import BaseModel

class Curso():
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo