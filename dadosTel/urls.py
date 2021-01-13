
from django.contrib import admin
from django.urls import path, include
from tel.views import TelefoneViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('tel', TelefoneViewSet, basename='tel')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
