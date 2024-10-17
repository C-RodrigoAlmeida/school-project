from rest_framework import generics

from src.courses.models import Course
from src.courses.serializers import CourseSerializer

class BaseCourseView:
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    class Meta:
        abstract = True

class CoursesAPIView(BaseCourseView, generics.ListCreateAPIView):
    pass

class CourseAPIView(BaseCourseView, generics.RetrieveDestroyAPIView):
    pass