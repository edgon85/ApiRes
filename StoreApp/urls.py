from django.conf.urls import url, include
from StoreApp import views
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

router.register(r'course', views.CourseAppViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)