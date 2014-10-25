# -*- encoding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator, validate_email
from django.core.exceptions import ValidationError

# Create your models here.

class Ruta (models.Model):
	nombre = models.CharField(max_length=100)
	creacion = models.DateTimeField(auto_now=False, auto_now_add=True,)
	actualizacion = models.DateTimeField(auto_now=True, auto_now_add=False,)

	def __unicode__(self):
		return self.nombre


class Cliente (models.Model):
	rfc = models.CharField(max_length=25, verbose_name='R.F.C.', validators=[RegexValidator(
				regex = r'[A-Z,Ñ,&]{3,4}[0-9]{2}[0-1][0-9][0-3][0-9][A-Z,0-9]?[A-Z,0-9]?[0-9,A-Z]?',
				message = u'Es un R.F.C. invalido',
				code = 'invalid_rfc',
			)])
	nombre = models.CharField(max_length=150)
	apellidos = models.CharField(max_length=150)
	direccion = models.CharField(max_length=250, verbose_name='Dirección')
	ciudad = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)
	cp = models.IntegerField(default=0, verbose_name='C.P.')
	email = models.CharField(max_length=100, verbose_name='E-mail', validators=[validate_email])
	telefono = models.CharField(max_length=25, verbose_name='Teléfono')
	creacion = models.DateTimeField(auto_now=False, auto_now_add=True,)
	actualizacion = models.DateTimeField(auto_now=True, auto_now_add=False,)
	ruta = models.ForeignKey('Ruta', verbose_name="Rutas")

	def __unicode__(self):
		return '%s' % (self.nombre)

class Proveedor (models.Model):
	nombre = models.CharField(max_length=150)
	apellidos = models.CharField(max_length=150)
	direccion = models.CharField(max_length=250, verbose_name='Dirección')
	ciudad = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)
	cp = models.IntegerField(default=0,  verbose_name='C.P.')
	email = models.CharField(max_length=100, verbose_name='E-mail', validators=[validate_email])
	telefono = models.CharField(max_length=25, verbose_name='Teléfono')
	empresa = models.CharField(max_length=150)
	creacion = models.DateTimeField(auto_now=False, auto_now_add=True,)
	actualizacion = models.DateTimeField(auto_now=True, auto_now_add=False,)

	class Meta:
		verbose_name='Proveedor'
		verbose_name_plural='Proveedores'

	def __unicode__(self):
		return '%s' % (self.nombre)


class Producto (models.Model):
	BICICLETA = 0
	MOTOCICLETA = 1
	TIPO_PRODUCTO = (
		(BICICLETA, 'Bicicleta'),
		(MOTOCICLETA, 'Motocicleta'),
	)

	NO = 0
	SI = 1
	FACTURADO = (
		(SI, 'Si'),
		(NO, 'No'),
	)

	cantidad = models.IntegerField(default=0)
	nombre = models.CharField(max_length=150)
	precio = models.DecimalField(max_digits=8, decimal_places=2,)
	tipo = models.IntegerField(choices=TIPO_PRODUCTO, default=BICICLETA)
	facturado = models.IntegerField(choices=FACTURADO, default=NO)
	reserva = models.IntegerField(default=0)
	fila = models.CharField(max_length=10)
	anaquel = models.IntegerField(default=0)
	nivel = models.IntegerField(default=0)
	anotacion = models.TextField()
	creacion = models.DateTimeField(auto_now=False, auto_now_add=True,)
	actualizacion = models.DateTimeField(auto_now=True, auto_now_add=False,)
	proveedor = models.ForeignKey('Proveedor', verbose_name='Proveedores')

	def __unicode__(self):
		return '%s' % (self.nombre)


class Pedido (models.Model):
	descuento = models.IntegerField(default=0)
	pagado = models.IntegerField(default=0)
	terminado = models.IntegerField(default=0);
	nota = models.CharField(max_length=250)
	creacion = models.DateTimeField(auto_now=False, auto_now_add=True,)
	actualizacion = models.DateTimeField(auto_now=True, auto_now_add=False,)
	cliente = models.ForeignKey('Cliente')
	productos = models.ManyToManyField('Producto', through='ProductosEnPedido', editable=False)

	def __unicode__(self):
		return '%s' % (self.creacion)


class ProductosEnPedido (models.Model):
	cantidad = models.IntegerField(default=True)
	producto = models.ForeignKey('Producto')
	pedido = models.ForeignKey('Pedido')
	creacion = models.DateTimeField(auto_now=False, auto_now_add=True,)
	actualizacion = models.DateTimeField(auto_now=True, auto_now_add=False,)

