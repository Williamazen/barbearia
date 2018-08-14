from django.db import models
from django.utils import timezone
import datetime
from datetime import timedelta

class Service(models.Model):
    class Meta:
     verbose_name="Serviço"
    name = models.CharField('nome',max_length=50)
    price = models.DecimalField('preço',max_digits=7, decimal_places=2)
    #image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) cara, tu falou q imagem n precisava né
    def __str__(self):
        return self.name

class Offer(models.Model):
    class Meta:
     verbose_name="Promoçõe"
    name = models.CharField('nome',max_length=50)
    discount = models.PositiveIntegerField('desconto')
    def __str__(self):
        return self.name


class Barber(models.Model):
    class Meta:
     verbose_name="barbeiro"
    name = models.CharField('nome',max_length=30)

    def __str__(self):
        return self.name
class OfferService(models.Model):
   class Meta:
    verbose_name="Promoções/Produto"
   idService = models.ForeignKey(Service, verbose_name = 'serviço', on_delete=models.CASCADE)
   idOffer = models.ForeignKey(Offer, verbose_name='Promoção', on_delete=models.CASCADE)

   def __str__(self):
        return self.idService.name+' '+self.idOffer.name

class Customer(models.Model):
    class Meta:
     pass
     verbose_name="Cliente"
    DDD = models.CharField(max_length=2)
    num_Tel = models.CharField('telefone', max_length=9)
    name = models.CharField('nome', max_length=30)
    email = models.EmailField('email', max_length=64)
    data_Nasc = models.DateField('data de nascimento')
    def __str__(self):
        return self.name
    class Meta:
        unique_together = (("DDD", "num_Tel"),)
    def get_absolute_url(self):

     return u'/index'   
   
class HistoryS(models.Model):
    class Meta:
     verbose_name="Registro"
    idBarb = models.ForeignKey(Barber, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('data',default=timezone.now)
    valor = models.DecimalField(max_digits=7,decimal_places=2)
    

    def __str__(self):
        
        #barbeiro = HistoryS.objects.get(idBarb=self.idBarb)
        #x=barbeiro.idBarb.name
        nome=self.idBarb.name
        data = self.pub_date - timedelta(hours=3)
        return 'serviço feito em:'+ data.strftime("%d-%m-%Y às %H:%M:%S") +'. por: '+ nome +  '. com ganho de: '+str(self.valor)
    
    
        

    #DateTimeField: default=timezone.now - from django.utils.timezone.now()