from rest_framework import routers
from .views import UserProfileViewSet

router = routers.DefaultRouter()
router.register('profile', UserProfileViewSet, 'profile')

urlpatterns = router.urls
