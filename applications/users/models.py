from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(_("username"), max_length=255, unique=True)
    is_teacher = models.BooleanField(
        _("Is teacher"), default=False, help_text=_("Is user is teacher")
    )
    is_staff = models.BooleanField(
        _("Is staff"), default=False, help_text=_("Is user can login into admin site")
    )
    is_superuser = models.BooleanField(
        _("Is superuser"),
        default=False,
        help_text=_("Is user can login into admin site and have all permissions"),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255)
    userpic = models.ImageField(_("User picture"), upload_to="userpics/%Y/%m/%d")
    country = models.CharField(_("country"), max_length=100)
    phone = models.CharField(_("phone number"), unique=True, max_length=14)
    city = models.CharField(_("city"), max_length=255)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
