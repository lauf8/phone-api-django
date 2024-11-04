from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from person.views import PersonViewSet
from number.views import NumberViewSet
from call.views import CallRegsiterViewSet, CallViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'number', NumberViewSet, basename='number')
router.register(r'call', CallViewSet, basename='call')
router.register(r'call-register', CallRegsiterViewSet, basename='call-register')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('call/',include('call.urls')),
    path('number/',include('number.urls')),
]
