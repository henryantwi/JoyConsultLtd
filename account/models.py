import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
    Permission
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


# class Customer(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_("email address"), unique=True)
#     full_name = models.CharField(max_length=150)
#     mobile = models.CharField(max_length=150, blank=True)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     objects = CustomAccountManager()
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = [
#         "full_name",
#     ]
#
#     groups = models.ManyToManyField(
#         Group,
#         related_name='customer_set',
#         blank=True,
#         help_text=_("Groups this user belongs to."),
#         related_query_name='customer'
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='customer_set',
#         blank=True,
#         help_text=_("Specific permissions for this user."),
#         related_query_name='customer'
#     )
#
#     class Meta:
#         verbose_name = "Account"
#         verbose_name_plural = "Accounts"
#
#     def __str__(self):
#         return self.full_name


# class Address(models.Model):
#     """
#     Address
#     """
#
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     customer = models.ForeignKey(
#         Customer, verbose_name=_("Customer"), on_delete=models.CASCADE
#     )
#     full_name = models.CharField(_("Full name"), max_length=150)
#     phone_number = models.CharField(_("Phone Number"), max_length=50)
#     postcode = models.CharField(_("Postcode"), max_length=50)
#     address_line_1 = models.CharField(_("Address Line 1"), max_length=255)
#     address_line_2 = models.CharField(_("Address Line 2"), max_length=255)
#     town_city = models.CharField(_("Town/City/State"), max_length=150)
#     delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
#     default = models.BooleanField(_("Default"), default=False)
#
#     class Meta:
#         verbose_name = "Address"
#         verbose_name_plural = "Addresses"
#
#     def __str__(self):
#         return self.full_name
