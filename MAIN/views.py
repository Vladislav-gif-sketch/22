from rest_framework import generics, viewsets
from .MainSerializer import MainSerializer

from .models import MAIN


class MainViewSet(viewsets.ModelViewSet):
    queryset = MAIN.objects.all()
    serializer_class = MainSerializer






# Create your views here.
