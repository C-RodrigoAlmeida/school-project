from rest_framework import serializers

from src.courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    model = Course

    fields = (
        "id",
        "title",
        "url",
        "created_at",
        "updated_at",
        "deleted_at"
    )