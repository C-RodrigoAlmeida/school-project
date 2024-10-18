from django.db import models
from src.core.models import BaseModel
from .course import Course

class Rating(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="ratings")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    commentary = models.TextField(blank=True, default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    
    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
        unique_together = ['email',  'course']
        ordering = ['-id']

    def __str__(self) -> str:
        return f'{self.name} rated the course {self.course} as {self.rating}'