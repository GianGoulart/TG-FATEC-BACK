from django.db import models

class Atletas(models.Model):
    idAtleta = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 50)
    enderecoCep = models.CharField(max_length = 9)
    enderecoRua = models.CharField(max_length = 50)
    enderecoNum = models.IntegerField(default=0)
    enderecoBairro = models.CharField(max_length = 50)
    dataNascimento = models.DateField()
    peso = models.DecimalField(decimal_places=2, max_digits=5)
    altura = models.DecimalField(decimal_places=2, max_digits=5)
    foto = models.ImageField()
    dataEntrada = models.DateField()
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
    telefone = models.CharField(max_length = 10)
    celular = models.CharField(max_length = 12)
    recado = models.CharField(max_length = 12)
    idAtleta = models.OneToOneField(Atletas, on_delete=models.CASCADE, primary_key = True)

    objects = models.Manager()

    def __str__(self):
        return str(self.idAtleta)