from rest_framework import serializers

from .models import *


class AppetizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appetizer
        fields = ['name', 'id']


class EntreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entree
        fields = ['name', 'id']


class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = ['name', 'id']
