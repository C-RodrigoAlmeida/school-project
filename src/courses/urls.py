from django.urls import path

from rest_framework.routers import SimpleRouter

from src.courses.controllers import (
    RatingAPIView,
    RatingsAPIView,
    CourseAPIView,
    CoursesAPIView,
    RatingsViewSet,
    CoursesViewSet,
)

router = SimpleRouter()
router.register("courses", CoursesViewSet)
router.register("ratings", RatingsViewSet)

urlpatterns = [
    path("courses/", CoursesAPIView.as_view(), name="courses"),
    path("courses/<int:pk>/", CourseAPIView.as_view(), name="courses"),

    path("courses/<int:course_pk>/ratings", RatingsAPIView.as_view(), name="course_ratings"),
    path("courses/<int:course_pk>/ratings/<int:ratings_pk>", RatingAPIView.as_view(), name="course_ratings"),


    path("ratings/", RatingsAPIView.as_view(), name="ratings"),
    path("ratings/<int:ratings_pk>/", RatingAPIView.as_view(), name="ratings"),
]
