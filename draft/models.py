from django.db import models
import datetime

class Atletas(models.Model):
    idAtleta = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 50,blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length = 90)
    enderecoCep = models.CharField(blank=True, null=True, max_length = 9)
    enderecoRua = models.CharField(blank=True, null=True, max_length = 50)
    enderecoNum = models.IntegerField(blank=True, null=True,default=0)
    enderecoBairro = models.CharField(blank=True, null=True,max_length = 50)
    cidade = models.CharField(blank=True, null=True,max_length = 50)
    dataNascimento = models.DateField(blank=True, null=True)
    peso = models.DecimalField(decimal_places=2, max_digits=5,blank=True, null=True)
    altura = models.DecimalField(decimal_places=2, max_digits=5,blank=True, null=True)
    foto = models.ImageField(blank=True, null=True)
    tipo = models.CharField(max_length = 10, choices=((1, 'ATLETA'),(2,'CANDIDATO')),blank=True, null=True)
    dataEntrada = models.DateTimeField(default = datetime.datetime.now,  blank=True, null=True)
    status = models.IntegerField(default=1)
    dataInativacao = models.DateField(blank=True, null=True)   

    objects = models.Manager()


    def __str__(self):
        return str(self.idAtleta)

class Skills(models.Model):
    idSkill = models.AutoField(primary_key = True)
    quarentaJardas = models.DecimalField(decimal_places=3, max_digits=5)
    supino = models.IntegerField(default=0)
    saltoVertical = models.DecimalField(decimal_places=2, max_digits=5)
    saltoHorizontal = models.DecimalField(decimal_places=2, max_digits=5)
    idAtleta = models.ForeignKey(Atletas, on_delete=models.CASCADE)
    dataAvaliacao = models.DateTimeField(default = datetime.datetime.now,  blank=True, null=True)
    objects = models.Manager()  

    def __str__(self):
        return str(self.idSkill)

class Posicao(models.Model):
    idPosicao = models.AutoField(primary_key = True)
    idTipoPosicao = models.IntegerField(default=0)
    descricao = models.CharField(max_length = 20)

    objects = models.Manager()

    def __str__(self):
        return str(self.idPosicao)

class Atletas_Posicao(models.Model):
    idAtletaPosicao = models.AutoField(primary_key = True)
    idAtleta = models.ForeignKey(Atletas, on_delete=models.CASCADE)
    idPosicao = models.ForeignKey(Posicao, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return str(self.idAtletaPosicao)

class Telefone(models.Model):
    telefone = models.CharField(max_length = 15, blank=True, null=True)
    celular = models.CharField(max_length = 15)
    recado = models.CharField(max_length = 15, blank=True, null=True)
    idAtleta = models.OneToOneField(Atletas, on_delete=models.CASCADE, primary_key = True)

    objects = models.Manager()

    def __str__(self):
        return str(self.idAtleta)

class DadosAtletas(models.Model):
    idAtleta = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length = 50)
    team = models.CharField(max_length = 10)
    posicao = models.CharField(max_length = 20)

    objects = models.QuerySet()

    def __str__(self):
        return str(self.idAtleta)

class Resultados(models.Model):        
    class Meta:
        managed: False

    nome = models.CharField(max_length = 50)
    quarentaJardas = models.DecimalField(decimal_places=3, max_digits=5)
    supino = models.IntegerField()
    saltoVertical = models.DecimalField(decimal_places=2, max_digits=5)
    saltoHorizontal = models.DecimalField(decimal_places=2, max_digits=5)
    idAtleta = models.IntegerField(primary_key = True)
    dataAvaliacao = models.DateTimeField()

    objects = models.QuerySet()

    def __str__(self):
        return str(self.idAtleta)
   
class Medias (models.Model):        
    class Meta:
        managed: False
    posicao = models.CharField(max_length = 20)
    idPosicao = models.IntegerField(primary_key = True)
    quarentaJardas = models.DecimalField(decimal_places=3, max_digits=5)
    supino = models.IntegerField()
    saltoVertical = models.DecimalField(decimal_places=2, max_digits=5)
    saltoHorizontal = models.DecimalField(decimal_places=2, max_digits=5)

    objects = models.QuerySet()

    def __str__(self):
        return str(self.idAtleta)
