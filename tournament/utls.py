from django.conf.urls import url, include

from rest_framework import routers

from .views import TournamentViewSet, ParticipantViewSet

router = routers.DefaultRouter()
router.register(r'tournament', TournamentViewSet)
router.register(r'participant', ParticipantViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
