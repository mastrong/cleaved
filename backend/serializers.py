from rest_framework import serializers

from .models import *


class AppetizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appetizer
        fields = ['name']


class EntreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entree
        fields = ['name']


class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = ['name']
