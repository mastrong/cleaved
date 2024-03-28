from django.db import models


class Appetizer(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Entree(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
