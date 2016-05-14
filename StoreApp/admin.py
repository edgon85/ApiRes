from django.contrib import admin
from .models import CourseApp

# Register your models here.

class CourseAppAdmin(admin.ModelAdmin):
	list_display = ["name","author"]
	class Meta:
		model = CourseApp


admin.site.register(CourseApp, CourseAppAdmin)