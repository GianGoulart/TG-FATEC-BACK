from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views    import APIView
from rest_framework import status

from .models import Atletas, Posicao, Skills, Telefone, Atletas_Posicao, DadosAtletas, Resultados, Medias 
from .serializers import AtletasSerializer, PosicaoSerializer, SkillsSerializer, TelefoneSerialiazer, Atletas_PosicaoSerializer, DadosAtletasSerializer, ResultadosSerializer, MediasSerializer

# Create your views here.
class AtletasList(generics.ListCreateAPIView):
    serializer_class = AtletasSerializer
    
    def get_queryset(self):
        queryset = Atletas.objects.all()
        tipo = self.request.query_params.get('tipo', None)
        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)
        return queryset

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Erro ao cadastrar"}, status=status.HTTP_409_CONFLICT)
    
    def put(self, request, pk, format=None):
        atleta = AtletasList.get_object(pk)
        serializer = self.serializer_class(atleta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        else:
            return Response({"message":"Erro ao cadastrar"}, status=status.HTTP_400_BAD_REQUEST)
    
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
    def get_queryset(self):
        queryset = Skills.objects.all()
        id = self.request.query_params.get('atleta', None)
        if id is not None:
            queryset = queryset.filter(idAtleta=id)
        return queryset
   
    serializer_class = SkillsSerializer

class SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class TelefonesList(generics.ListCreateAPIView):
    serializer_class = TelefoneSerialiazer

    def get_queryset(self):
        queryset = Atletas.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(idAtleta=id)
        return queryset

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Erro ao cadastrar"}, status=status.HTTP_409_CONFLICT)


class TelefonesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerialiazer

class Atletas_PosicoesList(generics.ListCreateAPIView):
    serializer_class = Atletas_PosicaoSerializer
    def get_queryset(self):
        queryset = Atletas_Posicao.objects.all()
        atleta = self.request.query_params.get('atleta', None)
        if atleta is not None:
            queryset = queryset.filter(idAtleta=atleta)
        return queryset

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Erro ao cadastrar"}, status=status.HTTP_409_CONFLICT)

class Atletas_PosicoesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atletas_Posicao.objects.all()
    serializer_class = Atletas_PosicaoSerializer

class DadosAtletasList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        atleta = self.request.query_params.get('atleta', None)
        if atleta == "0" or atleta is None :
            queryset = DadosAtletas.objects.raw('''
                    select  a.idAtleta idAtleta,
                            case b.idTipoPosicao
                                when 1 then "Ataque"
                                when 2 then "Defesa"
                                when 3 then "Especial"
                                end as team,
                            b.descricao posicao
                    from draft_atletas a, draft_posicao b, draft_atletas_posicao c
                    where 	a.idAtleta = c.idAtleta_id
                    and		b.idPosicao = c.idPosicao_id''')
    
        if atleta is not None:
            queryset = DadosAtletas.objects.raw('''
                select  a.idAtleta idAtleta,
                        case b.idTipoPosicao
                            when 1 then "Ataque"
                            when 2 then "Defesa"
                            when 3 then "Especial"
                            end as team,
                        b.descricao posicao
                from draft_atletas a, draft_posicao b, draft_atletas_posicao c
                where 	a.idAtleta = c.idAtleta_id
                and		b.idPosicao = c.idPosicao_id
                and     a.idAtleta = ''' + atleta)
        return queryset
    
    serializer_class = DadosAtletasSerializer

class DadosAtletasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DadosAtletas.objects.raw('''select 
                        case b.idTipoPosicao
                            when 1 then "Ataque"
                            when 2 then "Defesa"
                            when 3 then "Especial"
                            end as team,
                        b.descricao posicao
                from draft_atletas a, draft_posicao b, draft_atletas_posicao c
                where 	a.idAtleta = c.idAtleta_id
                and		b.idPosicao = c.idPosicao_id''')
    serializer_class = DadosAtletasSerializer

class ResultadosList(generics.ListCreateAPIView):
    def get_queryset(self):
        tipo = self.request.query_params.get('tipo', None)
        if tipo == "0" or tipo is None :
            queryset = Resultados.objects.raw('''select a.idAtleta idAtleta,
                                                        a.nome nome,
                                                        b.quarentaJardas quarentaJardas,
                                                        b.supino supino,
                                                        b.saltoHorizontal saltoHorizontal,
                                                        b.saltoVertical saltoVertical,
                                                        b.dataAvaliacao
                                                    from draft_atletas a, draft_skills b
                                                    where a.idAtleta = b.idAtleta_id''')
        if tipo is not None:
            queryset = Resultados.objects.raw('''select a.idAtleta idAtleta,
                                                        a.nome nome,
                                                        b.quarentaJardas quarentaJardas,
                                                        b.supino supino,
                                                        b.saltoHorizontal saltoHorizontal,
                                                        b.saltoVertical saltoVertical,
                                                        b.dataAvaliacao
                                                    from draft_atletas a, draft_skills b
                                                    where a.idAtleta = b.idAtleta_id
                                                    and   a.tipo = ''' + tipo)
        return queryset
    serializer_class = ResultadosSerializer 

class MediasList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Medias.objects.raw('''
                SELECT 	d.descricao posicao,
                        d.idPosicao,
                        avg(c.quarentaJardas) quarentaJardas,
                        avg(c.supino) supino,
                        avg(c.saltoHorizontal) saltoHorizontal,
                        avg(c.saltoVertical) saltoVertical
                FROM	draft_atletas a, draft_atletas_posicao b, draft_skills c, draft_posicao d
                where	a.idAtleta = b.idAtleta_id
                and		a.idAtleta= c.idAtleta_id
                and		b.idPosicao_id = d.idPosicao
                and     a.tipo = 1
                group by posicao;''')
    
        posicao = self.request.query_params.get('posicao', None)
        if posicao is not None:
            queryset = Medias.objects.raw('''
                SELECT 	d.descricao posicao,
                        d.idPosicao,
                        avg(c.quarentaJardas) quarentaJardas,
                        avg(c.supino) supino,
                        avg(c.saltoHorizontal) saltoHorizontal,
                        avg(c.saltoVertical) saltoVertical
                FROM	draft_atletas a, draft_atletas_posicao b, draft_skills c, draft_posicao d
                where	a.idAtleta = b.idAtleta_id
                and		a.idAtleta= c.idAtleta_id
                and		b.idPosicao_id = d.idPosicao
                and     a.tipo = 1
                and     d.idPosicao = '''+posicao +
                '''   group by posicao;''' )
        return queryset
    
    serializer_class = MediasSerializer

