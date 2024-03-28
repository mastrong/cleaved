from random import sample

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *


@api_view(['GET'])
def get_appetizer(request, format=None):
    if request.method == 'GET':
        appetizers = list(Appetizer.objects.all())
        appetizers = sample(appetizers, 4)
        shuffled_apps = [Appetizer.objects.filter(name=app).first() for app in appetizers][:4]

        serializer = AppetizerSerializer(shuffled_apps, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_entree(request, format=None):
    if request.method == 'GET':
        entrees = list(Entree.objects.all())
        entrees = sample(entrees, 4)
        shuffled_entrees = [Entree.objects.filter(name=entree).first() for entree in entrees][:4]

        serializer = EntreeSerializer(shuffled_entrees, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_dessert(request, format=None):
    if request.method == 'GET':
        desserts = list(Dessert.objects.all())
        desserts = sample(desserts, 4)
        shuffled_desserts = [Dessert.objects.filter(name=dessert).first() for dessert in desserts][:4]

        serializer = DessertSerializer(shuffled_desserts, many=True)
        return Response(serializer.data)
