from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Додаємо унікальне ім'я для зворотного зв'язку
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions_set",  # Додаємо унікальне ім'я для зворотного зв'язку
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
