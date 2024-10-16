from django.contrib import admin

from src.courses.models import Rating, Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'created_at', 'updated_at', 'deleted_at']
    search_fields = [ 'title', 'url']
    list_filter = ['created_at', 'updated_at', 'deleted_at']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'email', 'commentary', 'rating', 'created_at', 'updated_at', 'deleted_at']
    search_fields = ['course']
    list_filter = ['rating', 'created_at', 'updated_at', 'deleted_at']
