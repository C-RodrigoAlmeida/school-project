from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets

from src.courses.models import Rating
from src.courses.serializers import RatingSerializer

from django.db.models import QuerySet

class RatingBaseView:
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

"""
API V1
"""

class RatingsAPIView(RatingBaseView, generics.ListCreateAPIView):
    def get_queryset(self) -> QuerySet[Rating]:
        if not (course_pk := self.kwargs.get('course_pk')): return super().get_queryset()
        
        return self.queryset.filter(course_id=course_pk)

class RatingAPIView(RatingBaseView, generics.RetrieveDestroyAPIView):
    def get_object(self) -> Rating:
        if not (course_pk := self.kwargs.get('course_pk')): 
            return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('ratings_pk'))

        return get_object_or_404(self.get_queryset(), course_id=course_pk, pk=self.kwargs.get('ratings_pk'))
    

"""
API V2
"""

class RatingsViewSet(RatingBaseView, viewsets.ModelViewSet):
    pass