from rest_framework.views import APIView
from rest_framework.response import Response

from src.courses.serializers import RatingSerializer
from src.courses.models import Rating

class RatingAPIView(APIView):
    def get(self, request):
        return Response(RatingSerializer(
            Rating.objects.all(),
            many=True
        ).data)