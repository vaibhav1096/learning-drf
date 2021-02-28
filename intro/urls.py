from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, PlayerViewSet

router = DefaultRouter()

router.register('team', TeamViewSet, basename='team')
router.register('player', PlayerViewSet, basename='player')

urlpatterns = [
    path('', include(router.urls))
]
