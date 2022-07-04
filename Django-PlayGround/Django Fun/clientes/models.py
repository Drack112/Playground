from django.db import models

# Create your models here.
class Base(models.Model):
    online = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    celular = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to="avatar")

    def __str__(self) -> str:
        return self.nome
