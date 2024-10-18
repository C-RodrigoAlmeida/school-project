from django.db import models
from src.core.models import BaseModel

class Course(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-id']

    def __str__(self):
        return self.title