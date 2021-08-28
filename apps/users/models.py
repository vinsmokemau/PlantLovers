from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    second_last_name = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f'{self.username}'


class BuyerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    reputation = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Perfil de Comprador"
        verbose_name_plural = "Perfiles de Compradores"

    def __str__(self):
        return str(self.user)


class SellerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    reputation = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Perfil de Vendedor"
        verbose_name_plural = "Perfiles de Vendedores"

    def __str__(self):
        return str(self.user)
