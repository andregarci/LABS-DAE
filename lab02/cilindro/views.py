from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'titulo': "Volumen",
    }
    return render(request, 'cilindro/formulario.html', context)


def calcular(request):
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        radio = diametro / 2
        volumen = 3.1416 * radio ** 2 * altura
        return render(request, 'cilindro/respuesta.html', {'volumen': volumen})
    else:
        return render(request, 'cilindro/formulario.html')