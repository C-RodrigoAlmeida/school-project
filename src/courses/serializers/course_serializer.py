from rest_framework import serializers

from src.courses.models import Course

from rest_framework import serializers
from src.courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    ratings = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rating-detail')

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'created_at',
            'updated_at',
            'deleted_at',
            'ratings'
        ]
