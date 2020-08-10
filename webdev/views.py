from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): # primera vista

    p1 = Persona('Pablo "El loco"', 'Diaz')

    fecha_actual = datetime.datetime.now()

    doc_externo = open('C:/Users/tommy/Documents/Proyectos Programación/Proyectos Página Web/webdev/plantillas/mi_plantilla.html')

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({'nombre_persona':p1.nombre, 'apellido_persona':p1.apellido, 'momento_actual':fecha_actual})

    documento = plt.render(ctx)

    return HttpResponse(documento)

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