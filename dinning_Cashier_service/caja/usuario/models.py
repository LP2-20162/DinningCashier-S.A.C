from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    Esta tabla reemplaza al User de django auth
    """
    last_module_id = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
