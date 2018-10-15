from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^atletas/$', views.AtletasList.as_view(), name='atletas-list'),
    url(r'^atletas/(?P<pk>[0-9]+)/$', views.AtletasDetail.as_view(), name='atletas-detail'),

    url(r'^telefones/$', views.TelefonesList.as_view(), name='telefones-list'),
    url(r'^telefones/(?P<pk>[0-9]+)/$', views.TelefonesDetail.as_view(), name='telefones-detail'),
 
    url(r'^posicoes/$', views.PosicoesList.as_view(), name='posicoes-list'),
    url(r'^posicoes/(?P<pk>[0-9]+)/$', views.PosicoesDetail.as_view(), name='posicoes-detail'),

    url(r'^skills/$', views.SkillsList.as_view(), name='skills-list'),
    url(r'^skills/(?P<pk>[0-9]+)/$', views.SkillsDetail.as_view(), name='skills-detail'),

    url(r'^atletas-posicoes/$', views.Atletas_PosicoesList.as_view(), name='atletas_posicoes-list'),
    url(r'^atletas-posicoes/(?P<pk>[0-9]+)/$', views.Atletas_PosicoesDetail.as_view(), name='atletas_posicoes-detail'),

    url(r'^dados-atletas/$', views.DadosAtletasList.as_view(), name='dados-atletas-list'),
    url(r'^dados-atletas/(?P<pk>[0-9]+)/$', views.DadosAtletasDetail.as_view(), name='dados-atletas-detail'),

    url(r'^resultados/$', views.ResultadosList.as_view(), name='resultados-list'),
    
    url(r'^medias/$', views.MediasList.as_view(), name='resultados-list'),
]