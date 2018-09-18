from rest_framework import serializers
from .models import Atletas, Atletas_Posicao, Posicao, Telefone, Skills

class AtletasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atletas
        field = '__all__'
        exclude = ()


class Atletas_PosicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atletas_Posicao
        field = '__all__'
        exclude = ()

class PosicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posicao
        field = '__all__'
        exclude = ()

class TelefoneSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        field = '__all__'
        exclude = ()

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        field = '__all__'
        exclude = ()
