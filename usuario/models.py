from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser
from carrito.models import Carrito

class Usuario(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    cliente = models.BooleanField(null=False, default=True)
    activo = models.BooleanField(null=False, default=True)

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        if self.pk is None:  # El objeto se está creando
            self.cliente = True
        super(Usuario, self).save(*args, **kwargs)

    def productos_carro (self):
        return Carrito.objects.filter(usuario=self, activo=True, comprado=False)

    def carrito_count (self):
        return self.productos_carro().count()


class Meta:
    permissions = [
        ("change_cliente_activo", "Can change cliente and activo status"),
    ]
