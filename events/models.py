from django.db import models

# Create your models here.
class Evento(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.TextField("Descrição")
	foto = models.CharField(max_length=200)
	local = models.CharField(max_length=40)
	data = models.CharField(max_length=20)

	def __str__(self):
		return self.nome