from .views import *
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'employee', EmployeeViewSet, basename='employee')


urlpatterns = router.urls