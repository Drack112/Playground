from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters

from .serializers import ClienteSerializer

from .models import Cliente

# Create your views here.
class ClienteViewSet(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filters_backend = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = [
        "nome",
    ]
    search_fields = ["nome", "cpf"]

    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):
        return super(ClienteViewSet, self).dispatch(*args, **kwargs)
