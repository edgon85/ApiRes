from django import forms
from .models import CourseApp

class CourseAppForms(forms.ModelForm):
	class Meta:
		model = CourseApp
		fields = ['name','author','description',
					'rating',
					'students',
					'price',
					'photo']