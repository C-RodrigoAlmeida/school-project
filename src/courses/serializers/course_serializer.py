from rest_framework import serializers
from django.db.models import Avg

from src.courses.models import Course

from rest_framework import serializers
from src.courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    ratings = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rating-detail')

    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'created_at',
            'updated_at',
            'deleted_at',
            'ratings',
            'average_rating'
        ]

    def get_average_rating(self, object) -> float | None:
        average = object.ratings.aggregate(Avg('rating')).get('rating__avg')

        return round(average * 2) / 2 if average is not None else None