from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

from web.models import Platos,Empleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def PlatosVista(request):


    #Rutina para consulta de platos
    platosConsultados=Platos.objects.all()
    print(platosConsultados)


    #Esta vista va a utilizar un formulario de django
    #DEBO CREAR ENTONCES UN OBJETO DE LA CLASE FormularioPlatos()
    formulario=FormularioPlatos()

    #CREAMOS UN DICCIONARIO PARA ENVIAR EL FORMULARIO AL HTML(TEMPLATE)
    data={
        'formulario':formulario,
        'bandera':False,
        'platos':platosConsultados
    }

    if request.method=='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
            #creamos un objeto del tipo MODELO PLATO
            if datosPlato["tipo"] == '1' :
                t='Entrada'
            elif datosPlato["tipo"] == '2':
                t='Plato Fuerte'
            elif datosPlato["tipo"] == '3':
                t='Postre'
            
            platoNuevo=Platos(
                nombre=datosPlato["nombre"],
                descripcion=datosPlato["descripcion"],
                fotografia=datosPlato["fotografia"],
                precio=datosPlato["precio"],
                tipo=t
            )
            #Intentamos llevar el objeto platoNuevo a LA BD
            try:
                platoNuevo.save()
                data["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                print("error",error)
                data["bandera"]=False

    return render(request,'menuplatos.html',data)

def EmpleadosVista(request):

    empleadosConsultados = Empleados.objects.all()
    print(empleadosConsultados)

    formulario=FormularioEmpleados()

    data={
        'formulario':formulario,
        'bandera':False,
        'empleados':empleadosConsultados
    }

    if request.method == 'POST':

        datosDelFormulario = FormularioEmpleados(request.POST)
        if datosDelFormulario.is_valid():
            datosEmpleado = datosDelFormulario.cleaned_data
            if datosEmpleado["tipoempleado"] == '1' :
                t='cheff'
            elif datosEmpleado["tipoempleado"] == '2':
                t='Administrador'
            elif datosEmpleado["tipoempleado"] == '3':
                t='Mesero'
            else:
                t='Ayudante'
            empleadoNuevo=Empleados(
                nombre=datosEmpleado["nombre"],
                salario=datosEmpleado["salario"],
                direccion = datosEmpleado["direccion"],
                telefono = datosEmpleado["telefono"],
                tipoempleado = t,
                fotografia = datosEmpleado["fotografia"]
            )

            try:
                empleadoNuevo.save()
                data["bandera"]=True
                print("EXITO GUARDANDO AL EMPLEADO")
            except Exception as error:
                print("error",error)
                data["bandera"]=False
    return render(request,'menuempleados.html',data)
