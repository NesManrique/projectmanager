from django.contrib.auth.models import User, Group
from rest_framework import serializers, pagination
from projects.models import Project, Update
from django.core.paginator import Paginator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Update
		fields = ('id','creado','modificado','fecha_detalle','descripcion')

class ProjectSerializer(serializers.ModelSerializer):
	horas_totales = serializers.IntegerField(source='horas_totales',read_only=True)
	update_listing = serializers.HyperlinkedIdentityField(view_name='update-listing')

	class Meta:
		model = Project
		fields = ('id','creado','modificado','titulo','cliente','verticales','inicio','fin','horas_asig','horas_sem','horas_acum','horas_totales','status','detalle','consultores','lider','update_listing')
