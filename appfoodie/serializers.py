from rest_framework import serializers
from .models import Producto

class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = ('Nombre', 'Precio', 'Descripcion', 'Imagen')