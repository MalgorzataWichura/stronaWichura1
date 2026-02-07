from django.shortcuts import render, get_object_or_404, redirect
from .models import Warzywa, Miesa, Napoje, Pieczywo, Owoce

# --- WIDOKI STRON PRODUKTÓW ---

def szczegolynapoje(request, id):
    produkt = get_object_or_404(Napoje, id=id)
    # Dodajemy 'kategoria': 'napoje', żeby przycisk wiedział gdzie wysłać dane
    return render(request, 'szczegolynapoje.html', {'produkt': produkt, 'kategoria': 'napoje'})

def szczegolyowoce(request, id):
    produkt = get_object_or_404(Owoce, id=id)
    return render(request, 'szczegolyowoce.html', {'produkt': produkt, 'kategoria': 'owoce'})

def szczegolywarzywa(request, id):
    produkt = get_object_or_404(Warzywa, id=id)
    return render(request, 'szczegolywarzywa.html', {'produkt': produkt, 'kategoria': 'warzywa'})

def szczegolymiesa(request, id):
    produkt = get_object_or_404(Miesa, id=id)
    return render(request, 'szczegolymiesa.html', {'produkt': produkt, 'kategoria': 'miesa'})

def szczegolypieczywa(request, id):
    produkt = get_object_or_404(Pieczywo, id=id)
    return render(request, 'szczegolypieczywa.html', {'produkt': produkt, 'kategoria': 'pieczywo'})

# --- WIDOKI KOSZYKA ---

def pokaz_koszyk(request):
    koszyk = request.session.get('koszyk', {})
    suma = sum(item['cena'] * item['ilosc'] for item in koszyk.values())
    return render(request, 'koszyk.html', {'koszyk': koszyk, 'suma': suma})

def dodaj_do_koszyka(request, kategoria, id):
    tabele = {"warzywa": Warzywa, "miesa": Miesa, "napoje": Napoje, "owoce": Owoce, "pieczywo": Pieczywo}
    model = tabele.get(kategoria.lower())
    produkt = get_object_or_404(model, id=id)

    koszyk = request.session.get('koszyk', {})
    klucz = f"{kategoria}_{id}" 

    if klucz in koszyk:
        koszyk[klucz]['ilosc'] += 1
    else:
        koszyk[klucz] = {
            'nazwa': produkt.nazwa,
            'cena': produkt.cena,
            'ilosc': 1,
            'kategoria': kategoria,
            'id': id
        }
    
    request.session['koszyk'] = koszyk
    request.session.modified = True
    return redirect('pokaz_koszyk')

def usun_z_koszyka(request, klucz):
    koszyk = request.session.get('koszyk', {})
    if klucz in koszyk:
        del koszyk[klucz]
        request.session['koszyk'] = koszyk
        request.session.modified = True
    return redirect('pokaz_koszyk')

# --- STRONY LISTY ---

def sklep(request): 
    return render(request, 'stronastartowa.html')

def listaproduktowzkategorii(request, kategoria):
    tabele = {"warzywa": Warzywa, "miesa": Miesa, "napoje": Napoje, "owoce": Owoce, "pieczywo": Pieczywo}
    model = tabele.get(kategoria.lower())
    produkty = model.objects.all() if model else []
    return render(request, 'listaproduktowzkategorii.html', {"listaproduktowzkategorii": produkty, "kategoria": kategoria})