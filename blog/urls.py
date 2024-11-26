from django.urls import path



app_name = 'blog'


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('words/', views.words, name='words'),
    path('notes/', views.notes, name='notes'),
    path('about/', views.about, name='about'),
]
