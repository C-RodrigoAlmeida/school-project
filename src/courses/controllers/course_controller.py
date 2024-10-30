from rest_framework import generics

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from src.core.permissions import IsSuperUser
from src.courses.models import Course, Rating
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
    # permission_classes = (IsSuperUser,)

    @action(detail=True, methods=["get"])
    def ratings(self, request, pk=None):
        queryset = self.get_object().ratings.all()
        page = self.paginate_queryset(queryset)
        return (self.get_paginated_response(RatingSerializer(page, many=True).data) if page is not None
            else Response(RatingSerializer(queryset, many=True).data))