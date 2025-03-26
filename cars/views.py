from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all()
    # cars = Car.objects.filter(brand=5) # Acessa os campos pelo id na tabela Brand
    # cars = Car.objects.filter(brand__name= 'Fiat') # Essa é a forma que buscaria pelo name na tabela
    # cars = Car.objects.filter(model= 'Lancer') # Essa é a forma que buscaria pelo modelo do carro
    # cars = Car.objects.filter(model__contains= 'Lancer') # Essa é a forma que buscaria pelo modelo do carro não especificamente

    return render(
        request, 
        'cars.html',
        {'cars': cars }
    )


