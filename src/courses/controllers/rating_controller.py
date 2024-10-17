from rest_framework import generics

from src.courses.models import Rating
from src.courses.serializers import RatingSerializer

class RatingBaseView:
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingsAPIView(generics.ListCreateAPIView, RatingBaseView):
    pass

class RatingAPIView(generics.RetrieveDestroyAPIView, RatingBaseView):
    pass