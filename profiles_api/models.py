from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""

    # def __init__(self, arg):
    #     super(UserProfileManager, self).__init__()
    #     self.arg = arg

    def create_user(self, email, name, password=None):
        """Create a User Profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.ser_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, email, name, password):
        """Create a new Super User Profile with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database mode for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name =  models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FILED = 'name'

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name


    def __str__(self):
        """Return string representaion of our user"""
        return self.email
