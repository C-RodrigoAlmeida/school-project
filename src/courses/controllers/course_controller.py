from rest_framework.views import APIView
from rest_framework.response import Response

from src.courses.models import Course
from src.courses.serializers import CourseSerializer

class CourseAPIView(APIView):
    def get(self, request):
        return Response(CourseSerializer(
            Course.objects.all(),
            many=True
        ).data)