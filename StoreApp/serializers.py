from rest_framework import serializers
from .models import CourseApp


class CourseAppSerializer(serializers.ModelSerializer):

	class Meta:
		model = CourseApp
		fields = ('id','name', 'author', 'description', 'rating', 'students', 'price','photo')
