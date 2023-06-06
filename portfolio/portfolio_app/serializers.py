from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Habilidade

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

        
class HabilidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habilidade
        fields = '__all__'