from rest_framework import generics
from .models import Atletas, Posicao, Skills, Telefone, Atletas_Posicao 
from .serializers import AtletasSerializer, PosicaoSerializer, SkillsSerializer, TelefoneSerialiazer, Atletas_PosicaoSerializer

# Create your views here.
class AtletasList(generics.ListCreateAPIView):
    queryset = Atletas.objects.all()
    serializer_class = AtletasSerializer

class AtletasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atletas.objects.all()
    serializer_class = AtletasSerializer

class PosicoesList(generics.ListCreateAPIView):
    queryset = Posicao.objects.all()
    serializer_class = PosicaoSerializer

class PosicoesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posicao.objects.all()
    serializer_class = PosicaoSerializer

class SkillsList(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class TelefonesList(generics.ListCreateAPIView):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerialiazer

class TelefonesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerialiazer

class Atletas_PosicoesList(generics.ListCreateAPIView):
    queryset = Atletas_Posicao.objects.all()
    serializer_class = Atletas_PosicaoSerializer

class Atletas_PosicoesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atletas_Posicao.objects.all()
    serializer_class = Atletas_PosicaoSerializer
