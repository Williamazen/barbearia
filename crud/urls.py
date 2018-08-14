from django.urls import path

from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('<int:barber_id>/servico/', views.servico, name='servico'), #dps trocar por nome se quiser
    path('<int:barber_id>/confirma/', views.confirma, name='confirma'),
    path('new', views.CustomerCreate.as_view(), name='new'),
    path('ganhos',views.ganhos,name='ganhos')
]


