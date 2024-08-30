from django.db import models

# Create your models here.

class Aluno(models.Model):
    CIDADES_CHOICES = [
        ('RN', 'Natal'),
        ('RN', 'Pau dos Ferros'),
        ('RN', 'São Miguel'),
        ('RN', 'Alexandria'),
        ('RN', 'Tenente Ananias'),
        ('RN', 'Paraná'),
        ('RN', 'Luís Gomes'),
        ('RN', 'Caicó'),
        ('RN', 'Currais Novos'),
        ('CE', 'Pereiro')
    ]

    CURSO_CHOICES = [
        ('CS', 'Ciência da Computação'),
        ('ENG', 'Engenharia'),
        ('MED', 'Medicina'),
        ('ENF', 'Enfermagem'),
        ('DIR', 'Direito'),
        ('ARQ', 'Arquitetura'),
        ('FAR', 'Farmácia'),
        ('BM', 'Biomedicina'),
        ('LET', 'Letras')
    ]

    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=2, choices=CIDADES_CHOICES)
    email = models.EmailField()
    curso = models.CharField(max_length=3, choices=CURSO_CHOICES)

    def __str__(self):
        return self.nome
