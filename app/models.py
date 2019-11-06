from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)