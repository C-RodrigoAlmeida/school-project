from django.urls import path

from src.courses.controllers import RatingAPIView, RatingsAPIView, CourseAPIView, CoursesAPIView

urlpatterns = [
    path("courses/<int:pk>/", CourseAPIView.as_view(), name="courses"),
    path("courses/", CoursesAPIView.as_view(), name="courses"),
    path("ratings/<int:pk>/", RatingAPIView.as_view(), name="ratings"),
    path("ratings/", RatingsAPIView.as_view(), name="ratings"),
]
