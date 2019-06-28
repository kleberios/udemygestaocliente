from django.db import models

class Person(models.Model):
    primeiro_nome = models.CharField('Nome', max_length=20)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='foto_cliente', null=True, blank=True)

    def __str__(self):
        return self.primeiro_nome + ' ' + self.sobrenome

    class Meta:
        verbose_name_plural = 'Pessoas'
