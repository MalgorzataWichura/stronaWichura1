from django.shortcuts import render, get_object_or_404, redirect
from .models import Warzywa, Owoce, Napoje, Miesa, Pieczywo

# --- GŁÓWNE WIDOKI ---

def sklep(request):
    return render(request, 'stronastartowa.html')

def listaproduktowzkategorii(request, kategoria):
    tabele = {
        'warzywa': Warzywa,
        'owoce': Owoce,
        'napoje': Napoje,
        'miesa': Miesa,
        'pieczywo': Pieczywo,
    }
    model = tabele.get(kategoria)
    produkty = model.objects.all()
    return render(request, 'listaproduktowzkategorii.html', {
        "listaproduktowzkategorii": produkty, 
        "kategoria": kategoria
    })

# --- SZCZEGÓŁY (Detail Views) ---

def szczegolywarzywa(request, id):
    produkt = get_object_or_404(Warzywa, id=id)
    return render(request, 'szczegolywarzywa.html', {'produkt': produkt, 'kategoria': 'warzywa'})

def szczegolyowoce(request, id):
    produkt = get_object_or_404(Owoce, id=id)
    return render(request, 'szczegolyowoce.html', {'produkt': produkt, 'kategoria': 'owoce'})

def szczegolynapoje(request, id):
    produkt = get_object_or_404(Napoje, id=id)
    return render(request, 'szczegolynapoje.html', {'produkt': produkt, 'kategoria': 'napoje'})

def szczegolymiesa(request, id):
    produkt = get_object_or_404(Miesa, id=id)
    return render(request, 'szczegolymiesa.html', {'produkt': produkt, 'kategoria': 'miesa'})

def szczegolypieczywa(request, id):
    produkt = get_object_or_404(Pieczywo, id=id)
    return render(request, 'szczegolypieczywa.html', {'produkt': produkt, 'kategoria': 'pieczywo'})

# --- KOSZYK ---

def dodaj_do_koszyka(request, kategoria, id):
    tabele = {'warzywa': Warzywa, 'owoce': Owoce, 'napoje': Napoje, 'miesa': Miesa, 'pieczywo': Pieczywo}
    model = tabele.get(kategoria)
    produkt = get_object_or_404(model, id=id)
    
    koszyk = request.session.get('koszyk', {})
    klucz = f"{kategoria}_{id}"
    
    if klucz in koszyk:
        koszyk[klucz]['ilosc'] += 1
    else:
        koszyk[klucz] = {
            'nazwa': produkt.nazwa,
            'cena': str(produkt.cena),
            'ilosc': 1,
        }
    
    request.session['koszyk'] = koszyk
    return redirect('pokaz_koszyk')

def pokaz_koszyk(request):
    koszyk = request.session.get('koszyk', {})
    suma_calkowita = 0
    
    for klucz, dane in koszyk.items():
        dane['suma_produktu'] = float(dane['cena']) * dane['ilosc']
        suma_calkowita += dane['suma_produktu']
        
    return render(request, 'koszyk.html', {
        'koszyk': koszyk, 
        'suma_calkowita': suma_calkowita
    })

def zwieksz_ilosc(request, klucz):
    koszyk = request.session.get('koszyk', {})
    if klucz in koszyk:
        koszyk[klucz]['ilosc'] += 1
        request.session.modified = True
    return redirect('pokaz_koszyk')

def zmniejsz_ilosc(request, klucz):
    koszyk = request.session.get('koszyk', {})
    if klucz in koszyk:
        if koszyk[klucz]['ilosc'] > 1:
            koszyk[klucz]['ilosc'] -= 1
        else:
            del koszyk[klucz]  
        request.session.modified = True
    return redirect('pokaz_koszyk')


def zestawienie_bio(request):
    kontekst = {
        'warzywa': Warzywa.objects.filter(czy_bio=True),
        'owoce': Owoce.objects.filter(czy_bio=True),
        'napoje': Napoje.objects.filter(czy_bio=True),
        'miesa': Miesa.objects.filter(czy_bio=True),
        'pieczywo': Pieczywo.objects.filter(czy_bio=True),
    }
    return render(request, 'zestawienie_bio.html', kontekst)


def usun_produkt_warzywa(request, id):
    produkt = get_object_or_404(Warzywa, id=id)
    produkt.delete()
    return redirect('listaproduktowzkategorii', kategoria='warzywa')

def usun_produkt_owoce(request, id):
    produkt = get_object_or_404(Owoce, id=id)
    produkt.delete()
    return redirect('listaproduktowzkategorii', kategoria='owoce')

def usun_z_koszyka(request, klucz):
    koszyk = request.session.get('koszyk', {})
    if klucz in koszyk:
        del koszyk[klucz]
        request.session.modified = True
    return redirect('pokaz_koszyk')