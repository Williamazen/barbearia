from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum #até tentei, mas n foi dessa vez
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import HistoryS
from .models import Barber
from .models import Service
from .models import Offer
from .models import Customer

# Create your views here.
def ganhos(request):
    historico = HistoryS.objects.values('valor').annotate(tot=Sum('valor')).order_by('idBarb')#em teoria as querys do django foram feitas pra facilitar a vida, mas eu só me perdi nelas
    print(historico)
    context = {'nada':'nada'}
    return render(request, "crud/ganhos.html",context)
def index(request):
    barbeiros = Barber.objects.all()
    context = {'barbeiros' : barbeiros}
    return render(request, "crud/index.html",context)

def servico(request, barber_id):
    barbeiro = get_object_or_404(Barber, pk=barber_id)
    servicos = Service.objects.all()
    promocoes = Offer.objects.all()
    context = {'barbeiro' : barbeiro,'servicos' : servicos,'promocoes' : promocoes,}
    return render(request, "crud/servico.html",context)

def confirma(request, barber_id):
    barbeiro = get_object_or_404(Barber, pk=barber_id)
    promocoes = Offer.objects.all()
    servicos = Service.objects.all()
    servicos_selecionados = request.POST.getlist('servico')
    valor = 0
    soma = 0 
    for s in servicos_selecionados :                #eu sei q isso está horrível ,mas foi oq consegui, fiquei preso aqui 5 horas com erros de exceptions
        instance = list(Service.objects.values('price').filter(id=s)) #pra falar verdade, não sei nem como esse loop funcionou , mas funcionou, o problema é q
        print (instance)                                        # na  hora q vira dicionário, só tem uma chave 'price' pra valores diferentes
        for i in instance:
            soma = soma + i.get('price')                        #isso tá full php, pqp
            print (soma)
        
    promo_selecionadas = request.POST.get('promo')      
    for p in promo_selecionadas :                              
        insta = Offer.objects.values('discount').filter(id=p)
    for i in insta:
        disconto = i.get('discount')
    soma = (soma/100) * (100-disconto)
    print (soma)
    
    history = HistoryS(idBarb=barbeiro, valor=soma)
    history.save() 
    print(history)
    contexterror = {'promocoes' : promocoes,'barbeiro':barbeiro,'servicos' : servicos , 'error_message': "Você não selecionou um serviço"}
    #contextsucess = {'promocoes' : promocoes,'barbeiro':barbeiro,}
    if not servicos_selecionados : 
        return render(request, "crud/servico.html",contexterror)
    else :
        return HttpResponseRedirect(reverse('index'))    #precisa de uma mensagem falando q tudo deu certo kaka


class CustomerCreate(CreateView):
    model = Customer
    fields = ['name','DDD', 'num_Tel','email','data_Nasc']
    