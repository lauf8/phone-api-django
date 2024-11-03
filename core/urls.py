from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from person import views

router = DefaultRouter()
router.register(r'person', views.PersonViewSet, basename='perosn')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
