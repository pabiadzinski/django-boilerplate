from uuid import uuid4

from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    DEFAULT_AVATAR = 'img/avatar.svg'

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True, max_length=50)
    name = models.CharField(_('name'), max_length=50)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_avatar(self):
        if self.avatar:
            return settings.MEDIA_URL + self.avatar.name
        else:
            return settings.STATIC_URL + self.DEFAULT_AVATAR

    def __str__(self):
        return self.email
