from django.http import HttpResponse
import datetime

def saludo(request): # primera vista

    return HttpResponse('Hola Salinas esta es mi primera pagina con Django')

def despedida(request):

    return HttpResponse('Bye bye putos')

def dameFecha(request):

    fecha_actual = datetime.datetime.now()

    documento = '''<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>''' % fecha_actual

    return HttpResponse(documento)

def calcularEdad(request, agno):

    edadActual = 19
    periodo = agno - 2020
    edadFutura = edadActual + periodo
    documento = f'''<html>
    <body>
    En el año {agno} tendras {edadFutura}
    </body>
    </html>'''

    return HttpResponse(documento)