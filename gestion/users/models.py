from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("view_ventas","Puede ver la seccion de Ventas"),
            ("view_compras","Puede ver la seccion de compras"),
            ("view_inventarios", "Puede ver la seccion de Inventarios")
        ]
# Create your models here.
