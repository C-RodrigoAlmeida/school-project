from django.urls import path

from src.courses.controllers import RatingAPIView, CourseAPIView

urlpatterns = [
    path("courses/", CourseAPIView.as_view(), name="courses"),
    path("ratings/", RatingAPIView.as_view(), name="ratings")
]
