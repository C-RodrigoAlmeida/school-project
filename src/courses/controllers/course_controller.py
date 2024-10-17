from rest_framework import generics

from src.courses.models import Course
from src.courses.serializers import CourseSerializer

class BaseCourseView:
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    class Meta:
        abstract = True

class CoursesAPIView(generics.ListCreateAPIView, BaseCourseView):
    pass

class CourseAPIView(generics.RetrieveDestroyAPIView, BaseCourseView):
    pass