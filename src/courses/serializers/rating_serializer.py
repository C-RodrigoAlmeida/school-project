from rest_framework import serializers

from src.courses.models import Rating

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            "email": {"write_only": True}
        }

        model = Rating

        fields = (
            "id",
            "course",
            "name",
            "email",
            "commentary",
            "rating",
            "created_at",
            "updated_at",
            "deleted_at"
        )