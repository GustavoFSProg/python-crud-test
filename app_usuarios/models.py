from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField()
    idade = models.TextField()

    def __str__(self) -> str:
            return self.nome