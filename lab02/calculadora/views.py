from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'titulo': "Calculadora",
    }
    return render(request, 'calculadora/formulario.html', context)


def calcular(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        operacion = request.POST['operacion']

        if operacion == 'suma':
            respuesta = num1 + num2
        elif operacion == 'resta':
            respuesta = num1 - num2
        elif operacion == 'multiplicacion':
            respuesta = num1 * num2
        elif operacion == 'division':
            respuesta = num1 / num2
        context = {
            'num1': num1,
            'num2': num2,
            'operacion': operacion,
            'respuesta': respuesta,
        }

        return render(request, 'calculadora/respuesta.html', context)