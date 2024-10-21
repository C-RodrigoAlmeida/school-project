from rest_framework import serializers

from src.courses.models import Rating

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            "email": {"write_only": True}
        }
        model = Rating
        fields = [
            "id",
            "course",
            "name",
            "email",
            "commentary",
            "rating",
            "created_at",
            "updated_at",
            "deleted_at"
        ]

    def validate_rating(self, value):
        if value >= 0 and value <= 5: return value
        
        raise serializers.ValidationError('The rating has a to be a value between 0 and 5')