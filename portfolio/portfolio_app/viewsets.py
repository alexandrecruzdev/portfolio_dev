from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, HabilidadeSerializer
from .models import Habilidade
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer