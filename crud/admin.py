from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import OfferService
from .models import HistoryS
from .models import Service
from .models import Offer
from .models import Barber
from .models import Customer
#Register your models here.

admin.site.register(Service)
admin.site.register(Offer)
admin.site.register(OfferService)
admin.site.register(HistoryS)
admin.site.register(Barber)
admin.site.register(Customer)
admin.site.unregister(User)
admin.site.unregister(Group)



#from .models import 
