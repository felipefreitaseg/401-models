from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField()
    vivo = models.BooleanField(default=True)
    nacionalidade = models.CharField(max_length=50)

class Livro(models.Model):
    genero_aventura = 'av'
    genero_religioso = 'rl'
    genero_auto_ajuda = 'aa'
    genero_ficcao = 'fc'
    genero_scifi = 'sf'
    genero_terror = 'tr'
    genero_hq = 'hq'
    genero_manga = 'mg'
    genero_romance = 'rm'
    genero_biografia = 'bg'

    genero_opcoes = [
        (genero_aventura, 'Aventura'),
        (genero_religioso, 'Religioso'),
        (genero_auto_ajuda, 'Autoajuda'),
        (genero_ficcao, 'Ficção'),
        (genero_scifi, 'Ficção Cientifica'),
        (genero_terror, 'Terror'),
        (genero_hq, 'Histórias em Quadrinhos'),
        (genero_manga, 'Mangá'),
        (genero_romance, 'Romance'),
        (genero_biografia, 'Biografia')
    ]

    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=2, choices=genero_opcoes)
    dt_lançamento = models.DateField()
    descricao = models.TextField(default='')
    editora = models.CharField(max_length= 50, default='')
    preço = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    paginas = models.IntegerField()
    edicoes = models.IntegerField()
    nome = models.ForeignKey(Autor, on_delete=models.SET_DEFAULT, default='')
