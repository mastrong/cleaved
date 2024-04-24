from random import sample

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *


@api_view(['GET'])
def get_appetizer(request, format=None):
    if request.method == 'GET':
        appetizers = list(Appetizer.objects.all())
        appetizers = sample(appetizers, 4)
        shuffled_apps = [Appetizer.objects.filter(name=app).first() for app in appetizers]

        serializer = AppetizerSerializer(shuffled_apps, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_entree(request, format=None):
    if request.method == 'GET':
        entrees = list(Entree.objects.all())
        entrees = sample(entrees, 4)
        shuffled_entrees = [Entree.objects.filter(name=entree).first() for entree in entrees]

        serializer = EntreeSerializer(shuffled_entrees, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_dessert(request, format=None):
    if request.method == 'GET':
        desserts = list(Dessert.objects.all())
        desserts = sample(desserts, 4)
        shuffled_desserts = [Dessert.objects.filter(name=dessert).first() for dessert in desserts]

        serializer = DessertSerializer(shuffled_desserts, many=True)
        return Response(serializer.data)


def new_ingredients(request):
    if request.method == 'GET':
        if request.GET.get('appetizers') and request.GET.get('entrees') and request.GET.get('desserts'):
            appetizer_ids = request.GET.get('appetizers').split('-')
            appetizers = [Appetizer.objects.filter(id=app).first() for app in appetizer_ids]

            entree_ids = request.GET.get('entrees').split('-')
            entrees = [Entree.objects.filter(id=entree).first() for entree in entree_ids]

            desserts_ids = request.GET.get('desserts').split('-')
            desserts = [Dessert.objects.filter(id=dessert).first() for dessert in desserts_ids]
        else:
            appetizers = list(Appetizer.objects.all())
            appetizers = sample(appetizers, 4)

            entrees = list(Entree.objects.all())
            entrees = sample(entrees, 4)

            desserts = list(Dessert.objects.all())
            desserts = sample(desserts, 4)

            # update url to contain id of all ingredients - do in js
            # https://www.geeksforgeeks.org/how-to-modify-url-without-reloading-the-page-using-javascript/
            # window.history.replaceState({}, '', '""" + new_url + """/');
            # new_url = f"/{'-'.join(list(appetizer_dict.values()))}-{'-'.join(list(entree_dict.values()))}-{'-'.join(list(dessert_dict.values()))}/"
            # add script tag for js to get ingredients
            # https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#json-script
        ingredients = {
            'appetizers_': {app.name: app.id for app in appetizers},
            'entrees_': {entree.name: entree.id for entree in entrees},
            'desserts_': {dessert.name: dessert.id for dessert in desserts},
        }
        search_query = (
            f"?appetizers={'-'.join(list(str(_) for _ in ingredients['appetizers_'].values()))}"
            f"&entrees={'-'.join(list(str(_) for _ in ingredients['entrees_'].values()))}"
            f"&desserts={'-'.join(list(str(_) for _ in ingredients['desserts_'].values()))}"
        )
        context = {
            'ingredients': ingredients,
            'search_query': search_query
        }

        return render(request, 'frontend/index.html', context)
