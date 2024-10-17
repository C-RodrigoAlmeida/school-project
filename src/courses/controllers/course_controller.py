from rest_framework import generics

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from src.courses.models import Course
from src.courses.serializers import CourseSerializer, RatingSerializer

class BaseCourseView:
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    class Meta:
        abstract = True

"""
API V1
"""

class CoursesAPIView(BaseCourseView, generics.ListCreateAPIView):
    pass

class CourseAPIView(BaseCourseView, generics.RetrieveDestroyAPIView):
    pass


"""
API V2
"""
class CoursesViewSet(BaseCourseView, viewsets.ModelViewSet):
    @action(detail=True, methods=["get"])
    def ratings(self, request, pk=None):
        return Response(RatingSerializer(self.get_object().ratings.all(), many=True).data)