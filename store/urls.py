from django.urls import path
from . import views
from store.views import List
from .views import article_detail



urlpatterns = [
    path('contact' , views.Contact, name='contact'),
    path('update', views.update, name='update'),
    path('base', views.base, name='base'),
    path('about' ,views.about, name='about'),
    path('', List.as_view(), name='index'),
    path('recherche', views.recherche, name='recherche'),
    path('category', views.category, name='category'),
    path('culture', views.culture, name='culture'),
    path('catculture', views.catculture, name='catculture'),
    path('detail', views.detail, name='detail'),
    path('catsport', views.catsport, name='catsport'),
    path('introduction', views.introduction, name='introduction'),
    path('framework', views.framework, name='framework'),
    path('programme', views.programme, name='programme'),
    path('coder', views.coder, name='coder'),
    path('traitement', views.traitement, name='traitement'),
    path('cultur', views.cultur, name='cultur'),
    path('word', views.word, name='word'),
    path('js', views.js, name='js'),
    path('ph', views.ph, name='ph'),
]
