from rest_framework import generics

from src.courses.models import Rating
from src.courses.serializers import RatingSerializer

class RatingBaseView:
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingsAPIView(RatingBaseView, generics.ListCreateAPIView):
    pass

class RatingAPIView(RatingBaseView, generics.RetrieveDestroyAPIView):
    pass