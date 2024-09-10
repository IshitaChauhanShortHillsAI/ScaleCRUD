from .views import *
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet

router = DefaultRouter()
router.register(r'artist', ArtistViewSet, basename='artist')


urlpatterns = router.urls