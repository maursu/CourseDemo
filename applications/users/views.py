from rest_framework import permissions
from rest_framework import viewsets

from .models import UserProfile
from .serializers import UserProfileSerializer
from permissions.user_permissions import IsObjectOwner


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            self.permission_classes = [permissions.AllowAny]
        elif self.request.method == "POST":
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [IsObjectOwner, permissions.IsAuthenticated]
        return super().get_permissions()
