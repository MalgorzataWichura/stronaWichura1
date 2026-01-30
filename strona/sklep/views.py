from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Warzywa, Miesa, Napoje, Pieczywo, Owoce
from django.template import loader
from django.http import HttpResponse
def sklep(request): 
    template = loader.get_template('stronastartowa.html')
    return HttpResponse(template.render({},request))
def listaproduktowzkategorii(request, kategoria):
    tabele = {"warzywa": Warzywa, "miesa": Miesa, "napoje": Napoje, "owoce": Owoce, "pieczywo": Pieczywo}
    produkty = tabele.get(kategoria)
    listaproduktowzkategorii = produkty.objects.all()
    template = loader.get_template('listaproduktowzkategorii.html')
    context = {"listaproduktowzkategorii":listaproduktowzkategorii, "kategoria":kategoria}
    return HttpResponse(template.render(context,request))
def szczegolymiesa(request, id):
    produkt = get_object_or_404(Miesa, id = id)
    context = {"produkt":produkt}
    template = loader.get_template('szczegolymiesa.html')
    return HttpResponse(template.render(context,request))
    


# Create your views here.
