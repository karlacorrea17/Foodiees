from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from .forms import FormularioCliente
from .forms import FormularioRestaurante
from .forms import FormularioProducto
from .forms import FormularioPedido
from .forms import FormularioModificar
from .forms import FormularioModificarRes
from .forms import FormularioModificarPro
from .forms import FormularioModificarPed
from .forms import FormularioClientes
from .forms import FormularioLogin
from .models import Cliente
from .models import Restaurante
from .models import Producto
from .models import Pedido
from .models import UserProfile
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
#login
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#registro
from django.contrib.auth.models import User
#rest-frameworl
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SurveySerializer 
# Create your views here.



def inicio(request):
	f=FormularioCliente(request.POST or None)
	context={
		"f":clientes,
	}
	return render(request,"inicio.html",context)

def listar(request):
	clientes=Cliente.objects.all()
	context={
		'clientes':clientes,
	}
	return render(request,"listar.html",context)

def listarCli(request):
	clientes=Cliente.objects.all()
	context={
		'clientes':clientes,
	}
	return render(request,"listarCli.html",context)

def listarRes(request):
	restaurantes=Restaurante.objects.all()
	context={
		'restaurantes':restaurantes,
	}
	return render(request,"listarRes.html",context)

def listarPro(request):
	productos=Producto.objects.all()
	context={
		'productos':productos,
	}
	return render(request,"listarPro.html",context)

def listarPed(request):
	pedidos=Pedido.objects.all()
	context={
		'pedidos':pedidos,
	}
	return render(request,"listarPed.html",context)

def crear(request):
	f=FormularioCliente(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			c = Cliente()
			c.Nombre=datos.get("Nombre")
			c.Apellido=datos.get("Apellido")
			c.Cedula=datos.get("Cedula")
			c.Direccion=datos.get("Direccion")
			c.Telefono=datos.get("Telefono")
			c.Correo=datos.get("Correo")
			if c.save() != True:
				return redirect(listarCli)
	context= {
		"f":f,
	}
	return render(request, "crear.html", context)

def crearRes(request):
	res=FormularioRestaurante(request.POST or None)
	if request.method == 'POST':
		if res.is_valid():
			datos = res.cleaned_data
			r= Restaurante()
			r.Nombre=datos.get("Nombre")
			r.Gerente=datos.get("Gerente")
			r.Direccion=datos.get("Direccion")
			r.Telefono=datos.get("Telefono")
			if r.save() != True:
				return redirect(listarRes)
	context= {
		"res":res,
	}
	return render(request, "crearRes.html", context)



def crearPro(request):
	pro=FormularioProducto(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if pro.is_valid():
			datos = pro.cleaned_data
			re= Producto()
			re.idPro=datos.get("idPro")
			re.Nombre=datos.get("Nombre")
			re.Precio=datos.get("Precio")
			re.Descripcion=datos.get("Descripcion")
			re.Imagen=datos.get("Imagen")
			if re.save() != True:
				return redirect(listarPro)
	context= {
		"pro":pro,
	}
	return render(request, "crearPro.html", context)


def crearPed(request):
	pe=FormularioPedido(request.POST or None)
	if request.method == 'POST':
		if pe.is_valid():
			datos = pe.cleaned_data
			p= Pedido()
			p.idPed=datos.get("idPed")
			p.Cliente=datos.get("Cliente")
			p.Cantidad=datos.get("Cantidad")
			p.PrecioTotal=datos.get("PrecioTotal")
			if p.save() != True:
				return redirect(listarPed)
	context= {
		"pe":pe,
	}
	return render(request, "crearPed.html", context)

def modificar(request):
	f=FormularioModificar(request.POST or None)
	id=request.GET['id']
	c=Cliente.objects.get(id=id)
	f.fields['Nombre'].initial = c.Nombre
	f.fields['Apellido'].initial =  c.Apellido
	f.fields['Cedula'].initial = c.Cedula
	f.fields['Direccion'].initial = c.Direccion
	f.fields['Telefono'].initial = c.Telefono
	f.fields['Correo'].initial = c.Correo
	if f.is_valid():
		datos=f.cleaned_data
		c.Nombre=datos.get("Nombre")
		c.Apellido=datos.get("Apellido")
		c.Cedula=datos.get("Cedula")
		c.Direccion=datos.get("Direccion")
		c.Telefono=datos.get("Telefono")
		c.Correo=datos.get("Correo")
		if c.save() != True:
				return redirect(listarCli)
	context={
		'mod':'Modificar Cliente: '+c.Nombre+" "+c.Apellido,
		'form':f,
	}
	return render(request,"modificar.html",context)


def modificarRes(request):
	f=FormularioModificarRes(request.POST or None)
	id=request.GET['id']
	c=Restaurante.objects.get(id=id)
	f.fields['Nombre'].initial = c.Nombre
	f.fields['Gerente'].initial =  c.Gerente
	f.fields['Direccion'].initial = c.Direccion
	f.fields['Telefono'].initial = c.Telefono
	if f.is_valid():
		datos=f.cleaned_data
		c.Nombre=datos.get("Nombre")
		c.Gerente=datos.get("Gerente")
		c.Direccion=datos.get("Direccion")
		c.Telefono=datos.get("Telefono")
		if c.save() != True:
				return redirect(listarRes)
	context={
		'mod':'Modificar Restaurante: '+c.Nombre+" "+c.Gerente,
		'form':f,
	}
	return render(request,"modificarRes.html",context)


def modificarPro(request):
	f=FormularioModificarPro(request.POST or None)
	id=request.GET['id']
	c=Producto.objects.get(id=id)
	f.fields['Nombre'].initial = c.Nombre
	f.fields['Precio'].initial =  c.Precio
	f.fields['Descripcion'].initial = c.Descripcion
	f.fields['Imagen'].initial = c.Imagen
	if f.is_valid():
		datos=f.cleaned_data
		c.Nombre=datos.get("Nombre")
		c.Precio=datos.get("Precio")
		c.Descripcion=datos.get("Descripcion")
		c.Imagen=datos.get("Imagen")
		if c.save() != True:
				return redirect(listarPro)
	context={
		'mod':'Modificar Producto: '+c.Nombre+" "+c.Descripcion,
		'form':f,
	}
	return render(request,"modificarPro.html",context)


def modificarPed(request):
	f=FormularioModificarPed(request.POST or None)
	id=request.GET['id']
	c=Pedido.objects.get(id=id)
	f.fields['Cliente'].initial = c.Cliente
	f.fields['Cantidad'].initial =  c.Cantidad
	f.fields['PrecioTotal'].initial = c.PrecioTotal
	if f.is_valid():
		datos=f.cleaned_data
		c.Cliente=datos.get("Cliente")
		c.Cantidad=datos.get("Cantidad")
		c.PrecioTotal=datos.get("PrecioTotal")
		if c.save() != True:
				return redirect(listarPed)
	context={
		'mod':'Modificar Pedido: '+c.Cliente,
		'form':f,
	}
	return render(request,"modificarPed.html",context)

def eliminar(request):
	c=Cliente.objects.get(id=request.GET['id'])
	c.delete()
	return redirect(listarCli)


def eliminarRes(request):
	c=Restaurante.objects.get(id=request.GET['id'])
	c.delete()
	return redirect(listarRes)


def eliminarPro(request):
	c=Producto.objects.get(id=request.GET['id'])
	c.delete()
	return redirect(listarPro)



def eliminarPed(request):
	c=Pedido.objects.get(id=request.GET['id'])
	c.delete()
	return redirect(listarPed)


def registrar(request):
	if request.method == 'POST':
		r = FormularioClientes(request.POST, request.FILES)
		if r.is_valid():
			datos = r.cleaned_data
			ci = datos.get('ci')
			nombres = datos.get('nombres')
			apellidos = datos.get('apellidos')
			username = datos.get('username')
			password = datos.get('password')
			direccion = datos.get('direccion')
			email = datos.get('email')
			telefono = datos.get('telefono')
			photo = datos.get('photo')
			# Instanciamos un objeto User, con el username y password
			user_model = User.objects.create_user(username=username, password=password)
			# Añadimos datos personales
			user_model.first_name = nombres
			user_model.last_name = apellidos
			user_model.email = email
			# Y guardamos el objeto, esto guardara los datos en la db.
			user_model.save()
			# Ahora, creamos un objeto UserProfile, aunque no haya incluido
			# una imagen, ya quedara la referencia creada en la db.
			user_profile = UserProfile()
			# Al campo user le asignamos el objeto user_model
			user_profile.user = user_model
			# y le asignamos la photo (el campo, permite datos null)
			user_profile.photo = photo
			# Por ultimo, guardamos tambien el objeto UserProfile
			user_profile.save()
			# Ahora, redireccionamos a la pagina gracias.html
			# Pero lo hacemos con un redirect.
			return redirect(reverse("Gracias", kwargs={'username':username}))
	else:
		r = FormularioClientes()
		context = {
			'r': r,
		}
		return render(request, "registrar.html", context)

def gracias(request, username):
    return render(request, "gracias.html", {'username': username})

def usuario(request):
	if request.user.is_authenticated():
		return redirect(reverse("Inicio"))

	mensaje = None
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse("Inicio"))
			else:
				mensaje = "Tu usuario esta inactivo"
		#else:
		mensaje = "Nombre de Usuario y/o Contraseña incorrecto"
	return render(request, "login.html", {"mensaje":mensaje})

def salir(request):
	logout(request)
	return redirect('Login')


def list(request):
	query = Cliente.objects.all()
	query = serializers.serialize('json',query)
	return HttpResponse(query, 'application/json')

def listRes(request):
	query = Restaurante.objects.all()
	query = serializers.serialize('json',query)
	return HttpResponse(query, 'application/json')

def listPro(request):
	query = Producto.objects.all()
	query = serializers.serialize('json',query)
	return HttpResponse(query, 'application/json')

def listPed(request):
	query = Pedido.objects.all()
	query = serializers.serialize('json',query)
	return HttpResponse(query, 'application/json')

@api_view(['GET', 'POST'])
def survey_list(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = SurveySerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SurveySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def logout_view(request):
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    return redirect(reverse('appfoodie.login'))